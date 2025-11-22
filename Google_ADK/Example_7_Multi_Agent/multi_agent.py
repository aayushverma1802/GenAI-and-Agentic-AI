"""
Example 7: Multi-Agent
Multiple agents working together using Google ADK.
"""

from google.adk import LlmAgent
from google.adk.core import RunConfig

# Your API key
API_KEY = "AIzaSyBc-qTU8SgP2A_p2vwpnKuM3SU1gItrhKE"

def main():
    """Run a multi-agent example."""
    print("=== Multi-Agent Example ===\n")
    
    # Create two different specialized agents
    agent_researcher = LlmAgent(
        model="gemini-2.0-flash-exp",
        api_key=API_KEY,
        system_instruction="You are a research assistant. Provide concise, factual summaries."
    )
    
    agent_analyst = LlmAgent(
        model="gemini-2.0-flash-exp",
        api_key=API_KEY,
        system_instruction="You are an analyst. Provide detailed analysis and insights."
    )
    
    config = RunConfig()
    
    # Agent 1: Research task
    print("Agent 1 (Researcher): Summarizing AI developments...")
    response1 = agent_researcher.run(
        "Summarize the latest developments in AI in 3-4 sentences.",
        config=config
    )
    summary = response1.content
    print(f"Agent 1 Response: {summary}\n")
    
    # Agent 2: Analysis task based on Agent 1's output
    print("Agent 2 (Analyst): Analyzing the summary...")
    response2 = agent_analyst.run(
        f"Based on the following summary, provide a brief analysis of the key trends: {summary}",
        config=config
    )
    print(f"Agent 2 Response: {response2.content}\n")
    
    # Agent 1: Follow-up task
    print("Agent 1 (Researcher): Providing more details...")
    response3 = agent_researcher.run(
        "Based on your previous summary, provide more details about one specific AI development.",
        config=config
    )
    print(f"Agent 1 Response: {response3.content}\n")
    
    print("="*50)

if __name__ == "__main__":
    main()
