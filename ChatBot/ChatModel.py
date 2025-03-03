from langchain_huggingface import HuggingFaceEndpoint 
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
load_dotenv()
llm=HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)

# AI forgets what was the previous context
# That's why we use the chat_history
chat_history=[
    SystemMessage(content="You are a helpful AI assistant")
]

while True:
    user_input=input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if(user_input=="exit"):
        break
    result=llm.invoke(chat_history)
    chat_history.append(AIMessage(content=result))
    print("AI: ",result)
print(chat_history)

    