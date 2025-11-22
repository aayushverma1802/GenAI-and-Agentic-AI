"""
Example 8: Stateful Multi-Agent
Multiple agents that maintain state and share context using Google ADK.
"""

from google.adk import LlmAgent
from google.adk.core import RunConfig, Session

# Your API key
API_KEY = "AIzaSyBc-qTU8SgP2A_p2vwpnKuM3SU1gItrhKE"

def main():
    """Run a stateful multi-agent example."""
    print("=== Stateful Multi-Agent Example ===\n")
    
    # Create two agents with shared session
    shared_session = Session()
    
    agent1 = LlmAgent(
        model="gemini-2.0-flash-exp",
        api_key=API_KEY,
        system_instruction="You are a memory agent. Remember important information."
    )
    
    agent2 = LlmAgent(
        model="gemini-2.0-flash-exp",
        api_key=API_KEY,
        system_instruction="You are an assistant agent. Use information from the memory agent."
    )
    
    config1 = RunConfig(session=shared_session)
    config2 = RunConfig(session=shared_session)
    
    # Agent 1: Store information
    print("Agent 1: Storing user preferences...")
    response1 = agent1.run(
        "Remember the following user preferences: "
        "Favorite color: Blue, Favorite food: Pizza, Favorite programming language: Python",
        config=config1
    )
    print(f"Agent 1: {response1.content}\n")
    
    # Agent 2: Try to recall (should have access to shared session)
    print("Agent 2: Trying to recall user preferences...")
    response2 = agent2.run(
        "What is the user's favorite color and food?",
        config=config2
    )
    print(f"Agent 2: {response2.content}\n")
    
    # Agent 1: Continue with stored context
    print("Agent 1: Using stored context...")
    response3 = agent1.run(
        "Based on the user's preferences, suggest a weekend activity.",
        config=config1
    )
    print(f"Agent 1: {response3.content}\n")
    
    # Display shared session history
    print("=== Shared Session History ===")
    for message in shared_session.messages:
        role = message.role
        content = message.content[:100] if len(message.content) > 100 else message.content
        print(f"{role}: {content}...")
    
    print("\n" + "="*50)

if __name__ == "__main__":
    main()
