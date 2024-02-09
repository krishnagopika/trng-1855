import unittest

from langchain_core.outputs import LLMResult

from src.main.lab import questions, execute_json_agent
from src.utilities.llm_testing_util import llm_connection_check, llm_wakeup, classify_relevancy


class TestLLMResponses(unittest.TestCase):

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

    def test_execute_json_agent(self):
        response = execute_json_agent()
        self.assertIsInstance(response, list)
        self.assertEqual(len(response), 2)
        self.assertIsInstance(response[0], str)
        self.assertIsInstance(response[1], str)
        self.assertTrue(classify_relevancy(response[0], questions[0]))
        self.assertTrue(classify_relevancy(response[1], questions[1]))


if __name__ == "__main__":
    unittest.main()