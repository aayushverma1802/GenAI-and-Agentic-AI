"""
Example 6: Persistent Storage
An agent that saves and loads sessions for persistence using Google ADK.
"""

from google.adk import LlmAgent
from google.adk.core import RunConfig, Session
import json
import os

# Your API key
API_KEY = "AIzaSyBc-qTU8SgP2A_p2vwpnKuM3SU1gItrhKE"
STORAGE_FILE = "chat_session.json"

def save_session(session: Session):
    """Save session to a JSON file."""
    session_data = {
        "messages": [
            {"role": msg.role, "content": msg.content}
            for msg in session.messages
        ]
    }
    
    with open(STORAGE_FILE, 'w') as f:
        json.dump(session_data, f, indent=2)
    print(f"Session saved to {STORAGE_FILE}")

def load_session() -> Session:
    """Load session from a JSON file."""
    if not os.path.exists(STORAGE_FILE):
        return Session()
    
    with open(STORAGE_FILE, 'r') as f:
        session_data = json.load(f)
    
    session = Session()
    # Restore messages to session
    for msg_data in session_data.get("messages", []):
        session.add_message(msg_data["role"], msg_data["content"])
    
    return session

def main():
    """Run a persistent storage example."""
    print("=== Persistent Storage Example ===\n")
    
    # Create an agent
    agent = LlmAgent(
        model="gemini-2.0-flash-exp",
        api_key=API_KEY
    )
    
    # Try to load existing session
    session = load_session()
    
    if session.messages:
        print("Found saved session with previous messages.")
        print("Creating new session to continue conversation...\n")
    
    # Create a new session
    session = Session()
    config = RunConfig(session=session)
    
    # Add new messages
    print("User: Tell me a fun fact about space.")
    response1 = agent.run("Tell me a fun fact about space.", config=config)
    print(f"Agent: {response1.content}\n")
    
    print("User: What's the largest planet in our solar system?")
    response2 = agent.run("What's the largest planet in our solar system?", config=config)
    print(f"Agent: {response2.content}\n")
    
    # Save the session
    save_session(session)
    
    print("\n" + "="*50)

if __name__ == "__main__":
    main()
