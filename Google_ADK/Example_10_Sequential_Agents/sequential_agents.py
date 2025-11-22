"""
Example 10: Sequential Agents
Agents that execute tasks in a specific sequence using Google ADK Sequential workflow.
"""

from google.adk import LlmAgent
from google.adk.workflows import Sequential
from google.adk.core import RunConfig

# Your API key
API_KEY = "AIzaSyBc-qTU8SgP2A_p2vwpnKuM3SU1gItrhKE"

def main():
    """Run a sequential agents example."""
    print("=== Sequential Agents Example ===\n")
    
    # Create agents for different stages
    agent_researcher = LlmAgent(
        model="gemini-2.0-flash-exp",
        api_key=API_KEY,
        system_instruction="You are a research agent. Gather and summarize information."
    )
    
    agent_writer = LlmAgent(
        model="gemini-2.0-flash-exp",
        api_key=API_KEY,
        system_instruction="You are a writer. Create engaging content based on research."
    )
    
    agent_editor = LlmAgent(
        model="gemini-2.0-flash-exp",
        api_key=API_KEY,
        system_instruction="You are an editor. Review and improve content."
    )
    
    config = RunConfig()
    
    # Step 1: Research
    print("Step 1: Research Phase")
    print("Researcher Agent: Gathering information...")
    research_response = agent_researcher.run(
        "Research and provide 5 key facts about quantum computing.",
        config=config
    )
    research_data = research_response.content
    print(f"Research Output:\n{research_data}\n")
    
    # Step 2: Writing
    print("Step 2: Writing Phase")
    print("Writer Agent: Creating content based on research...")
    writing_response = agent_writer.run(
        f"Based on the following research, write a short article (3-4 paragraphs) about quantum computing:\n\n{research_data}",
        config=config
    )
    article = writing_response.content
    print(f"Article:\n{article}\n")
    
    # Step 3: Editing
    print("Step 3: Editing Phase")
    print("Editor Agent: Reviewing and improving the article...")
    editing_response = agent_editor.run(
        f"Review the following article and suggest improvements for clarity and engagement:\n\n{article}",
        config=config
    )
    print(f"Editor's Feedback:\n{editing_response.content}\n")
    
    # Step 4: Final revision
    print("Step 4: Final Revision")
    print("Writer Agent: Incorporating editor's feedback...")
    final_response = agent_writer.run(
        f"Original article:\n{article}\n\nEditor's feedback:\n{editing_response.content}\n\n"
        "Please revise the article incorporating the feedback.",
        config=config
    )
    print(f"Final Article:\n{final_response.content}\n")
    
    print("="*50)

if __name__ == "__main__":
    main()
