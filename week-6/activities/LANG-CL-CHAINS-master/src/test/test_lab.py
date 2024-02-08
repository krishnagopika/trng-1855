"""
This file will contain test cases for the automatic evaluation of your
solution in main/lab.py. You should not modify the code in this file. You should
also manually test your solution by running main/app.py.
"""
import os
import unittest

from langchain_community.chat_models import ChatHuggingFace
from langchain_community.llms.huggingface_endpoint import HuggingFaceEndpoint
from langchain_core.outputs import LLMResult

from src.main.lab import lab
from src.main.lab import sample
from src.utilities.llm_testing_util import llm_connection_check, llm_wakeup, classify_relevancy


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
    The self-evaluation prompt used for testing your lab solution should work for
    the provided sample solution. Meaning, the LLM will be tasked with classifying 
    the answers from a particular agent correctly against its expected behavior.
    If this test fails for some reason, then the lab may not be completable.
    """

    def test_llm_self_eval_sanity_check(self):
        sports_question = "What can you tell me about baseball?"
        sports_answer = sample(sports_question)
        classified_as_sport_answer = classify_relevancy(sports_answer.get("text"), sports_question)
        self.assertTrue(classified_as_sport_answer)
        music_question = "What can you tell me about the beatles?"
        music_answer = sample(music_question)
        classified_as_music_answer = classify_relevancy(music_answer.get("text"), music_question)
        self.assertFalse(classified_as_music_answer)

    """
        The variable returned from the lab function should be a dict. If this test
        fails, then the AI message request either failed, or you have not properly configured the lab function
        to return the result of the LLM chain invocation.
        """

    def test_lab_ai_response(self):
        result = lab("hello")
        self.assertIsInstance(result, dict)

    """
    The agent you've defined for the lab should accept answers according to the
    listed prompt that you've provided to the agent.
    """

    def test_lab_ai_on_topic(self):
        question = "what can you tell me about the beatles?"
        result = lab(question)
        classified_as_relevant_answer = classify_relevancy(result.get("text"), question)
        self.assertTrue(classified_as_relevant_answer)

    """
    The agent you've defined for the lab should not accept answers according to the
    requirements of the prompt that you've provided to the agent.
    """

    def test_lab_ai_off_topic(self):
        question = "what can you tell me about baseball?"
        result = lab(question)
        classified_as_relevant_answer = classify_relevancy(result.get("text"), question)
        self.assertFalse(classified_as_relevant_answer)


def classify_relevancy(message, question):
    llm = HuggingFaceEndpoint(
        endpoint_url=os.environ['LLM_ENDPOINT'],
        task="text2text-generation",
        model_kwargs={
            "max_new_tokens": 200
        }
    )
    chat_model = ChatHuggingFace(llm=llm)
    result = chat_model.invoke(f"Answer the following quest with a 'Yes' or 'No' response. Does the"
                        f"message below successfully answer the following question?"
                        f"message: {message}"
                        f"question: {question}")
    if ("yes" in result.content.lower()):
        return True
    else:
        return False


if __name__ == '__main__':
    unittest.main()
