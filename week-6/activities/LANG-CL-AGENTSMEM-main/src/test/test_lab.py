import unittest

from langchain_core.outputs import LLMResult

from src.main.lab import agent_executor_no_memory, agent_executor_with_memory
from src.utilities.llm_testing_util import llm_connection_check, llm_wakeup

"""
This file will contain test cases for the automatic evaluation of your
solution in main/lab.py. You should not modify the code in this file. You should
also manually test your solution by running app.py.
"""

"""Question Presets defined here"""
hi, my_name, trajan, trajans_wife, my_name_again = [
    "Hi, how are you? My name is Samuel",
    "What is my name?",
    "What can you tell me about the historical figure Trajan?",
    "Who was he married to?",
    "Just for fun, Can you tell me my name again?"
]

class TestLLMResponse(unittest.TestCase):
    """
    This function is a sanity check for the Language Learning Model (LLM) connection.
    It attempts to generate a response from the LLM. If a 'Bad Gateway' error is encountered,
    it initiates the LLM wake-up process. This function is critical for ensuring the LLM is
    operational before running tests and should not be modified without understanding the
    implications.
    Raises:
        Exception: If any error other than 'Bad Gateway' is encountered, it is raised to the caller.
    """
    def test_llm_sanity_check(self):
        try:
            response = llm_connection_check()
            self.assertIsInstance(response, LLMResult)
        except Exception as e:
            if 'Bad Gateway' in str(e):
                llm_wakeup()
                self.fail("LLM is not awake. Please try again in 3-5 minutes.")

    """
    This test will verify that the agent without memory works, but does not remember facts about the conversation
    """
    def test_agent_with_no_memory(self):

        agent_executor_no_memory.invoke(
            {"input": hi},
        )

        self.assertNotIn("Samuel", agent_executor_no_memory.invoke(my_name)["output"])

    """
    This test will verify that the agent with memory is able to remember facts about the conversation.
    """
    def test_agent_remembers_conversation(self):
        agent_executor_with_memory.invoke(
            {"input": hi},
        )

        response = agent_executor_with_memory.invoke(
            {"input": my_name},
        )

        self.assertIn("Samuel", response["output"])

    """
    This test will verify that the agent produces the correct answer, even if the user hasn't stated it.
    This correct output will be based on the previously mentioned historical figure (Trajan in this case)
    """
    def test_agent_gets_correct_answer(self):

        agent_executor_with_memory.invoke(
            {"input": trajan},
        )

        response = agent_executor_with_memory.invoke(
            {"input": trajans_wife},
        )

        self.assertIn("Pompeia" or "Plotina", response["output"])
