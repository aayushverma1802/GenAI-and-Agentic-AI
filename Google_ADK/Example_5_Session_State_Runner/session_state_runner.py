"""
Example 5: Session, State, & Runner
An agent that maintains conversational state using Google ADK.
"""

from google.adk import LlmAgent
from google.adk.core import RunConfig, Session

# Your API key
API_KEY = "AIzaSyBc-qTU8SgP2A_p2vwpnKuM3SU1gItrhKE"

def main():
    """Run a session state runner example."""
    print("=== Session, State, & Runner Example ===\n")
    
    # Create an agent
    agent = LlmAgent(
        model="gemini-2.0-flash-exp",
        api_key=API_KEY
    )
    
    # Create a session to maintain state
    session = Session()
    config = RunConfig(session=session)
    
    # First message
    print("User: Hello! My name is Alice.")
    response1 = agent.run("Hello! My name is Alice.", config=config)
    print(f"Agent: {response1.content}\n")
    
    # Second message - should remember the name
    print("User: What's my name?")
    response2 = agent.run("What's my name?", config=config)
    print(f"Agent: {response2.content}\n")
    
    # Third message - continuing the conversation
    print("User: Tell me a joke about programming.")
    response3 = agent.run("Tell me a joke about programming.", config=config)
    print(f"Agent: {response3.content}\n")
    
    # Display session history
    print("=== Session History ===")
    for message in session.messages:
        print(f"{message.role}: {message.content[:100]}...")
    
    print("\n" + "="*50)

if __name__ == "__main__":
    main()
