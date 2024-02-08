import langchain_core.messages.ai
from src.main.lab import sample
from src.main.lab import lab

"""
This file will contain some sample code to send the output of the functions in lab.py to the 
console. You may modify this file in any way, it will not affect the test results.
"""


def main():
    user_input = input("Enter some text here to prompt the sports chain to talk about sports:")
    result = sample(user_input)
    print(result)
    print("Now let's test the chain you've built, which should only accept music prompts.")
    user_input = input("Enter some text here to prompt the music chain to talk about music:")
    result = lab(user_input)
    print(result)

if __name__ == '__main__':
    main()
