# Agents with Toolkits Lab
The [`lab.py`](src/main/lab.py) file is the centerpiece of the Agents with Toolkits Lab, where you will be implementing 
and interacting with several toolkit classes provided by LangChain. The lab is designed to enhance your skills in handling 
working with JSON files through a toolkit provided by LangChain. Feel free to explore other [toolkits and agents
provided by LangChain here](https://python.langchain.com/docs/integrations/toolkits), as there are so many more. 
It connects to an external ChatGPT for practical application of these concepts. The ultimate goal of the lab is to 
pass all test cases provided in [`src/test/test_lab.py`](./src/test/test_lab.py).

# Files to modify
The code you should modify, as well as the instructions for completing the lab, are in [`src/main/lab.py`](src/main/lab.py). Take notice of
the TODO comments in the file, this contains all instructions for the implementations required to complete the lab.

You may modify [`app.py`](src/main/app.py), which is provided for manual testing.

You should ***NOT*** modify [`src/test/test_lab.py`](src/test/test_lab.py) or anything commented with "DO NOT TOUCH". You must pass all 
test cases provided to pass the lab.

# LLM Connection Overview
This lab leverages an external connection to a hosted LLM. It is possible that it may become inaccessible due to an 
invalid API key or the service being unavailable. **PRIOR** to beginning the labs you should run the `test_llm_sanity_check` 
test case in [`src/test/test_lab.py`](src/test/test_lab.py). The environment variables you should use for the connection should either be 
automatically configured for you upon opening the lab, or will be explicitly provided.