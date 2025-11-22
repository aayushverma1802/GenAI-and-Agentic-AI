"""
Example 3: LiteLLM Integration
An agent using LiteLLM with Google ADK.
"""

from google.adk import LlmAgent
from google.adk.core import RunConfig

# Your API key
API_KEY = "AIzaSyBc-qTU8SgP2A_p2vwpnKuM3SU1gItrhKE"

def main():
    """Run a LiteLLM agent example."""
    print("=== LiteLLM Agent Example ===\n")
    
    # Create an agent that can work with LiteLLM-compatible models
    # ADK supports various model providers through LiteLLM
    agent = LlmAgent(
        model="gemini/gemini-2.0-flash-exp",
        api_key=API_KEY
    )
    
    # Create run config
    config = RunConfig()
    
    # Run the agent
    response = agent.run(
        "Translate 'Hello, world!' to French, Spanish, and German.",
        config=config
    )
    
    print("Response:")
    print(response.content)
    print("\n" + "="*50)

if __name__ == "__main__":
    main()
