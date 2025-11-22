"""
Example 9: Callbacks
An agent that uses callbacks to handle events using Google ADK.
"""

from google.adk import LlmAgent
from google.adk.core import RunConfig, Callback

# Your API key
API_KEY = "AIzaSyBc-qTU8SgP2A_p2vwpnKuM3SU1gItrhKE"

class MyCallback(Callback):
    """Custom callback to handle agent events."""
    
    def on_run_start(self, run_id: str, input_data: str):
        """Called when a run starts."""
        print(f"[Callback] Run started: {run_id}")
        print(f"[Callback] Input: {input_data[:50]}...")
    
    def on_run_end(self, run_id: str, output_data: str):
        """Called when a run ends."""
        print(f"[Callback] Run ended: {run_id}")
        print(f"[Callback] Output: {output_data[:100]}...")
    
    def on_tool_call(self, tool_name: str, tool_input: dict):
        """Called when a tool is invoked."""
        print(f"[Callback] Tool called: {tool_name}")
        print(f"[Callback] Tool input: {tool_input}")

def main():
    """Run a callbacks agent example."""
    print("=== Callbacks Agent Example ===\n")
    
    # Create an agent
    agent = LlmAgent(
        model="gemini-2.0-flash-exp",
        api_key=API_KEY
    )
    
    # Create callback
    callback = MyCallback()
    
    # Create run config with callback
    config = RunConfig(callbacks=[callback])
    
    # Run the agent with callback
    print("Running agent with callbacks...\n")
    response = agent.run(
        "Tell me a short joke about programming.",
        config=config
    )
    
    print("\nFull Response:")
    print(response.content)
    print("\n" + "="*50)

if __name__ == "__main__":
    main()
