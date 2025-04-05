from typing import List, Dict
from langraph.graph import StateGraph, START, END
from langchain_ollama.llms import OllamaLLM

# Define the state structure
class State(dict):
    messages: List[Dict[str, str]]

# Create the graph builder
graph_builder = StateGraph(State)

# Load the Ollama LLM (ensure 'llama3.1' is available in Ollama locally)
llm = OllamaLLM(model='llama3.1')

# Define the chatbot node logic
def chatbot(state: State):
    response = llm.invoke(state["messages"])
    state["messages"].append({"role": "assistant", "content": response})
    return {"messages": state["messages"]}

# Add nodes and edges
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

# Compile the graph
graph = graph_builder.compile()

# Function to stream updates from the graph
def stream_graph_updates(user_input: str):
    state = {"messages": [{"role": "user", "content": user_input}]}
    for update in graph.stream(state):
        for value in update.values():
            print("Assistant:", value["messages"][-1]["content"])

# Main loop to run the chatbot
if __name__ == '__main__':
    while True:
        try:
            user_input = input("User: ")
            if user_input.lower() in ["quit", "exit", "q"]:
                print("Goodbye!")
                break
            stream_graph_updates(user_input)
        except Exception as e:
            print(f"An error occurred: {e}")
            break
