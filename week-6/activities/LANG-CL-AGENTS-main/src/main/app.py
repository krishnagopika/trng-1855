from main.lab import agent_executor

"""
This file will contain some sample code that invokes the agent with two different tasks.
If the lab is completed correctly, the console should show the agent determining which tool to use for the job. 
You may modify this file in any way, it will not affect the test results.
NOTE: The agent will occasionally trip over itself and start talking to itself. 
Either be more descriptive in your tools descriptions, or just run app.py again if it worked previously.
"""


def main():

    userinput1 = input("Enter a word to find the length: ")
    res1 = agent_executor.invoke("How many letters are in the word " + userinput1 + "?")

    print("Response Object: ", res1)
    print(res1["output"])

    print("=========")

    userinput2 = input("Enter an integer (preferably from 1-10) to find the cube: ")
    res2 = agent_executor.invoke("What is the cube of " + userinput2 + "?")

    print("Response Object: ", res2)


if __name__ == '__main__':
    main()
