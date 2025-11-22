# Google ADK (Agent Development Kit) Examples

This repository contains 12 comprehensive examples of Google ADK agent development using the official [Google Agent Development Kit](https://google.github.io/adk-docs/).

## About Google ADK

The Agent Development Kit (ADK) is a flexible and modular framework for developing and deploying AI agents. While optimized for Gemini and the Google ecosystem, ADK is model-agnostic, deployment-agnostic, and built for compatibility with other frameworks.

## Setup

1. **Install the required packages:**
```bash
pip install -r requirements.txt
```

2. **API Key Configuration:**
   - The API key is already configured in each example file: `AIzaSyBc-qTU8SgP2A_p2vwpnKuM3SU1gItrhKE`
   - If you need to change it, update the `API_KEY` variable in each Python file.

3. **Python Version:**
   - ADK Python v1.19.0+ requires Python 3.10 or higher

## Examples

### Example 1: Basic Agent
A simple LLM agent that generates text responses.
```bash
python Example_1_Basic_Agent/basic_agent.py
```

### Example 2: Tools
An agent with custom function tools.
```bash
python Example_2_Tools/tools_agent.py
```

### Example 3: LiteLLM
Integration with LiteLLM for model management.
```bash
python Example_3_LiteLLM/litellm_agent.py
```

### Example 4: Structured Output
An agent that generates structured JSON responses.
```bash
python Example_4_Structured_Output/structured_output_agent.py
```

### Example 5: Session, State, & Runner
An agent that maintains conversational state across multiple interactions.
```bash
python Example_5_Session_State_Runner/session_state_runner.py
```

### Example 6: Persistent Storage
An agent that saves and loads chat sessions for persistence.
```bash
python Example_6_Persistent_Storage/persistent_storage.py
```

### Example 7: Multi-Agent
Multiple agents working together to perform complex tasks.
```bash
python Example_7_Multi_Agent/multi_agent.py
```

### Example 8: Stateful Multi-Agent
Multiple agents that maintain state and share context.
```bash
python Example_8_Stateful_Multi_Agent/stateful_multi_agent.py
```

### Example 9: Callbacks
An agent that uses callbacks to handle events during execution.
```bash
python Example_9_Callbacks/callbacks_agent.py
```

### Example 10: Sequential Agents
Agents that execute tasks in a specific sequence, passing results between them.
```bash
python Example_10_Sequential_Agents/sequential_agents.py
```

### Example 11: Parallel Agents
Multiple agents running concurrently to handle different tasks simultaneously.
```bash
python Example_11_Parallel_Agents/parallel_agents.py
```

### Example 12: Loop Agents
An agent that performs iterative tasks in a loop.
```bash
python Example_12_Loop_Agents/loop_agents.py
```

## API Key

The API key used in all examples: `AIzaSyBc-qTU8SgP2A_p2vwpnKuM3SU1gItrhKE`

## Model

All examples use `gemini-2.0-flash-exp` model. You can change this to other available models.

## Resources

- [ADK Documentation](https://google.github.io/adk-docs/)
- [ADK Python GitHub](https://github.com/google/adk-python)
- [ADK Quickstart Guide](https://google.github.io/adk-docs/get-started/python/)

## Notes

- Make sure you have a stable internet connection to use the Google Gemini API
- Some examples may take longer to execute depending on the complexity of the tasks
- Example 6 creates a `chat_session.json` file for persistent storage
- Example 12 includes an interactive loop that requires user input
- Example 11 uses asyncio for parallel execution.

