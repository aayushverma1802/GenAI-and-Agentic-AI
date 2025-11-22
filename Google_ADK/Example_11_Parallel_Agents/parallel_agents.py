"""
Example 11: Parallel Agents
Multiple agents running concurrently using Google ADK Parallel workflow.
"""

from google.adk import LlmAgent
from google.adk.workflows import Parallel
from google.adk.core import RunConfig
import asyncio

# Your API key
API_KEY = "AIzaSyBc-qTU8SgP2A_p2vwpnKuM3SU1gItrhKE"

def main():
    """Run a parallel agents example."""
    print("=== Parallel Agents Example ===\n")
    
    # Create multiple agents
    agents = [
        LlmAgent(
            model="gemini-2.0-flash-exp",
            api_key=API_KEY
        ) for _ in range(5)
    ]
    
    # Define tasks for different agents
    tasks = [
        "Translate 'Hello, world!' to French, Spanish, and German.",
        "Summarize the plot of 'The Matrix' in 3 sentences.",
        "What's the capital of Japan and one interesting fact about it?",
        "Explain quantum computing in simple terms.",
        "List 5 benefits of regular exercise."
    ]
    
    config = RunConfig()
    
    # Run agents in parallel using asyncio
    async def run_parallel():
        async def agent_task(agent, task, task_id):
            try:
                print(f"[Agent {task_id}] Starting task...")
                response = agent.run(task, config=config)
                print(f"[Agent {task_id}] Completed")
                return {
                    "id": task_id,
                    "prompt": task,
                    "response": response.content,
                    "status": "success"
                }
            except Exception as e:
                print(f"[Agent {task_id}] Error: {e}")
                return {
                    "id": task_id,
                    "prompt": task,
                    "error": str(e),
                    "status": "error"
                }
        
        # Create tasks for all agents
        coroutines = [
            agent_task(agents[i], tasks[i], i+1)
            for i in range(len(agents))
        ]
        
        # Run all tasks in parallel
        results = await asyncio.gather(*coroutines)
        return results
    
    # Run parallel execution
    print("Starting all agents in parallel...\n")
    results = asyncio.run(run_parallel())
    
    # Display results
    print("\n" + "="*50)
    print("RESULTS")
    print("="*50)
    for result in results:
        print(f"\nAgent {result['id']}:")
        print(f"  Prompt: {result['prompt']}")
        if result['status'] == 'success':
            print(f"  Response: {result['response'][:150]}...")
        else:
            print(f"  Error: {result['error']}")
    
    print("\n" + "="*50)

if __name__ == "__main__":
    main()
