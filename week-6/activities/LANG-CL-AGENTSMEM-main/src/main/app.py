from src.main.lab import agent_executor_no_memory, agent_executor_with_memory

"""
This file contains some sample code that invokes conversational agents with and without memory.
If the lab is completed correctly, the agent will carry on a conversation in each invocation.
The agent will use its memory (ConversationBufferWindowMemory) to attempt to carry on the conversation.

The agent without memory will fail to accurately answer questions that require memory
    -("What's my name?" "Who did the historical figure marry?")
The agent with memory will have better luck answering these questions.

If you would like to see the agent's thought process, uncomment "verbose=True" in initialize_agent() found in lab.py

You may modify this file in any way, it will not affect the test results.

NOTE: On occasion, the agent may trip on itself and give an irregular/irrelevant response. This may be an ongoing
issue with how agents parse outputs. Don't hesitate to re-run app.py to see if it was a hallucination.
For now, we prevent an Exception being thrown by including handle_parsing_errors=True in initialize_agent().
"""

"""Question Presets defined here"""
question_list = [
    "Hi, how are you? My name is Samuel",
    "What is my name?",
    "What can you tell me about the historical figure Trajan?",
    "Who was he married to?",
    "Just for fun, Can you tell me my name again?"
]

def main():

    print("INVOKING AGENT WITHOUT MEMORY--------------------------------- ")

    for question in question_list:
        response = agent_executor_no_memory.invoke(
            {"input": question},
        )
        print(f"INPUT: {question}")
        print("OUTPUT: " + response["output"])

    print("INVOKING AGENT WITH MEMORY------------------------------------")
    for question in question_list:
        response = agent_executor_with_memory.invoke(
            {"input": question},
        )
        print(f"INPUT: {question}")
        print("OUTPUT: " + response["output"])


if __name__ == '__main__':
    main()
