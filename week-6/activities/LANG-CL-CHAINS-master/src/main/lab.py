import os

from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate

"""
Next, we will be working on producing LLM chains. A RAG application will feature multiple
steps of distinct LLM operations, for which they may be provided access to different prompts
and resources, each tailored to a specific task. Every one of those operations may be labelled 
as their own 'chain'. For now, let's create some LLM chains that are simply
built on a basic prompt, and make functions that will return the message from a chat with a specific 
chain.

https://python.langchain.com/docs/modules/chains/foundational/llm_chain
"""
# define llm

prompt1 = ("You are a language model that will talk about sports, and will not talk about anything else. "
           "Talk about: {user_input}")
sports_chain = LLMChain(llm=llm, prompt=PromptTemplate.from_template(prompt1))


def sample(user_input):
    return sports_chain(user_input)


"""
TODO: create a complimentary LLMChain that will talk about music, and will refuse all other prompt attempts.
Test cases will verify if the resulting message only creates relevant music responses.
"""
prompt2 = None
music_chain = None


def lab(user_input):
    return music_chain(user_input)
