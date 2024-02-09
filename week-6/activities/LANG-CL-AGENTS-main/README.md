# Overview

### Agents

- The goal of an Agent is to use an LLM and a prompt to **choose a sequence of actions to take.**
- They are designed to perform **well-defined tasks**, such as answering questions, summarizing text, translating languages, and mathematical operations.    
  - Its **inputs** are:
     - Tools: Descriptions of available tools (read below)
     - User Input: The objective, at a high level
     - Intermediate steps: Any action + tool output pairs that were previously executed to produce the User Input
  - Its **output** is *one* of the following:
     - AgentAction: The next action to take
     - AgentFinish: The final response to send to the user
- With regular chains, a sequence of actions is hardcoded. With agents, an LLM is used to determine which actions to take, and in which order. 

### Tools

- Tools are **functions that an agent can invoke**. There are two important design considerations around tools:
    - Giving the agent access to the tools it needs
    - Describing the tools in a way that is most helpful to the agent

- Tools are critical in building a working agent.
    - If an agent doesn't have access to the right set of tools, it can't accomplish the objectives you give it.
    - If the tools aren't described well, the agent won't know how to use them.

# Agents with Tools Lab

### Files to Modify:

- You will be directly modifying ```src/main/lab.py.```
  - Look for the "TODO" comments, which will specify the requirements for completing the lab. 
- You may modify ```app.py```, which already contains sample code that should provide a valid output upon completion of the lab.
- DO NOT modify ```src/main/labtest.py```, as it contains the tests that you must pass to complete the lab.
  - You can consider your lab complete when every test passes.


### Notes & Resources

- This lab utilizes an LLM over an external connection, and can become inaccessible for various reasons. Running ```test_llm_sanity_check``` in ```src/main/labtest.py``` can determine if a valid connection has been established. 
- Environment variables should be automatically configured for you upon opening the lab.

[LangChain Documentation on Agents](https://python.langchain.com/docs/modules/agents/)

[Creating Custom Tools](https://python.langchain.com/docs/modules/agents/tools/custom_tools)