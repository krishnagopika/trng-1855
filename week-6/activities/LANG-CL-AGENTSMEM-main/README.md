# Overview

### Memory

- Users of LLMs expect to have a **conversational interation** with AI. 
  - This requires a human-like tone, as well as the ability to **remember key points about the conversation.**
  - Most LLMs have the human tone down already. So it's our job to decide how to deal with memory.

- Langchain has quite a few ways to tackle memory management. We will be looking at **ConversationBufferWindowMemory**.
  - ConversationBufferWindowMemory stores a certain amount of previous interactions, specified by the "k" attribute.

# Conversational Agents with Memory Lab

- In this lab, we will be creating Conversational Agents with Memory provided by ConversationBufferWindowMemory
  - We will see an example of an agent with and without memory of previous interactions

### Files to Modify:

- You will be directly modifying ```src/main/lab.py.```
  - Look for the "TODO" comments, which will specify the requirements for completing the lab. 
- You may modify ```src/app.py```, which contains sample code that should provide a valid output upon lab completion.
- DO NOT modify ```src/main/labtest.py```, as it contains the tests that you must pass to complete the lab.
  - You can consider your lab complete when every test passes.


### Notes & Resources

- This lab utilizes an LLM over an external connection, and can become inaccessible for various reasons. Running ```test_llm_sanity_check``` in ```src/main/labtest.py``` can determine if a valid connection has been established. 
- Environment variables should be automatically configured for you upon opening the lab.

- [Langchain Docs on Agents with Memory](https://python.langchain.com/docs/modules/memory/agent_with_memory)
- [ConversationWindowBufferMemory](https://python.langchain.com/docs/modules/memory/types/buffer_window)