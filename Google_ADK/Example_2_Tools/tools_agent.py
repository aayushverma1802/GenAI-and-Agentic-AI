"""
Example 2: Tools
An agent with tools using Google ADK.
"""

from google.adk import LlmAgent
from google.adk.core import RunConfig
from google.adk.tools import FunctionTool

# Your API key
API_KEY = "AIzaSyBc-qTU8SgP2A_p2vwpnKuM3SU1gItrhKE"

def calculate_sum(a: float, b: float) -> float:
    """Calculate the sum of two numbers."""
    return a + b

def calculate_product(a: float, b: float) -> float:
    """Calculate the product of two numbers."""
    return a * b

def main():
    """Run a tools agent example."""
    print("=== Tools Agent Example ===\n")
    
    # Create custom tools
    sum_tool = FunctionTool(calculate_sum)
    product_tool = FunctionTool(calculate_product)
    
    # Create an agent with tools
    agent = LlmAgent(
        model="gemini-2.0-flash-exp",
        api_key=API_KEY,
        tools=[sum_tool, product_tool]
    )
    
    # Create run config
    config = RunConfig()
    
    # Run the agent with a task that requires tools
    response = agent.run(
        "What is the sum of 15 and 27? Then multiply that result by 3.",
        config=config
    )
    
    print("Response:")
    print(response.content)
    print("\n" + "="*50)

if __name__ == "__main__":
    main()
