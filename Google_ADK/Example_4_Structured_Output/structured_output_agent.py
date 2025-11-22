"""
Example 4: Structured Output
An agent that generates structured JSON responses using Google ADK.
"""

from google.adk import LlmAgent
from google.adk.core import RunConfig
import json

# Your API key
API_KEY = "AIzaSyBc-qTU8SgP2A_p2vwpnKuM3SU1gItrhKE"

def main():
    """Run a structured output agent example."""
    print("=== Structured Output Agent Example ===\n")
    
    # Create an agent with structured output instruction
    agent = LlmAgent(
        model="gemini-2.0-flash-exp",
        api_key=API_KEY,
        system_instruction="Always respond with valid JSON format."
    )
    
    # Create run config
    config = RunConfig()
    
    # Run the agent with structured output request
    response = agent.run(
        "Provide a JSON object with keys 'name', 'age', 'occupation', and 'hobbies' "
        "for a person named Alice who is 30 years old, works as a software engineer, "
        "and enjoys reading and hiking.",
        config=config
    )
    
    print("Structured Response:")
    print(response.content)
    
    # Try to parse and pretty print
    try:
        # Extract JSON from response if it's wrapped in markdown
        content = response.content
        if "```json" in content:
            content = content.split("```json")[1].split("```")[0].strip()
        elif "```" in content:
            content = content.split("```")[1].split("```")[0].strip()
        
        data = json.loads(content)
        print("\nParsed JSON:")
        print(json.dumps(data, indent=2))
    except json.JSONDecodeError:
        print("\n(Response is not valid JSON)")
    
    print("\n" + "="*50)

if __name__ == "__main__":
    main()
