"""
Example 1: Basic Agent
A simple LLM agent using Google ADK.
"""

from google.adk import LlmAgent
from google.adk.core import RunConfig

# Your API key
API_KEY = "AIzaSyBc-qTU8SgP2A_p2vwpnKuM3SU1gItrhKE"

def main():
    """Run a basic agent example."""
    print("=== Basic Agent Example ===\n")
    
    # Create a basic LLM agent
    agent = LlmAgent(
        model="gemini-2.0-flash-exp",
        api_key=API_KEY,
        system_instruction="You are a helpful assistant."
    )
    
    # Create run config
    config = RunConfig()
    
    # Run the agent
    response = agent.run(
        "Write a short story about a time-traveling historian.",
        config=config
    )
    
    print("Response:")
    print(response.content)
    print("\n" + "="*50)

if __name__ == "__main__":
    main()
