"""
Example 12: Loop Agents
An agent that performs iterative tasks in a loop using Google ADK Loop workflow.
"""

from google.adk import LlmAgent
from google.adk.workflows import Loop
from google.adk.core import RunConfig

# Your API key
API_KEY = "AIzaSyBc-qTU8SgP2A_p2vwpnKuM3SU1gItrhKE"

def main():
    """Run a loop agents example."""
    print("=== Loop Agents Example ===\n")
    
    # Create an agent
    agent = LlmAgent(
        model="gemini-2.0-flash-exp",
        api_key=API_KEY
    )
    
    config = RunConfig()
    
    # Example 1: Fixed loop
    print("Example 1: Fixed Loop (5 iterations)")
    print("-" * 50)
    
    for i in range(5):
        print(f"\nIteration {i+1}:")
        response = agent.run(
            f"Provide a fun fact about number {i+1}.",
            config=config
        )
        print(f"Response: {response.content}")
    
    # Example 2: Interactive loop
    print("\n\nExample 2: Interactive Loop")
    print("-" * 50)
    print("Enter 'exit' or 'quit' to stop the conversation.\n")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() in ['exit', 'quit', 'q']:
            print("\nExiting conversation. Goodbye!")
            break
        
        if not user_input:
            continue
        
        try:
            response = agent.run(user_input, config=config)
            print(f"Agent: {response.content}\n")
        except Exception as e:
            print(f"Error: {e}\n")
    
    # Example 3: Conditional loop with state
    print("\n\nExample 3: Conditional Loop with State")
    print("-" * 50)
    
    from google.adk.core import Session
    session = Session()
    config_with_session = RunConfig(session=session)
    
    questions = [
        "What is 2 + 2?",
        "What is the capital of France?",
        "What is the largest planet in our solar system?",
        "What is the speed of light?"
    ]
    
    correct_count = 0
    for i, question in enumerate(questions, 1):
        print(f"\nQuestion {i}: {question}")
        response = agent.run(question, config=config_with_session)
        print(f"Answer: {response.content}")
        
        # Simple check for correctness
        answer_lower = response.content.lower()
        if any(keyword in answer_lower for keyword in ["4", "four", "paris", "jupiter", "299792", "300000"]):
            correct_count += 1
            print("✓ Likely correct!")
        else:
            print("? (Uncertain)")
    
    print(f"\nTotal likely correct answers: {correct_count}/{len(questions)}")
    print("\n" + "="*50)

if __name__ == "__main__":
    main()
