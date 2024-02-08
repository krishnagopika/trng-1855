import os
import requests
from langchain_community.chat_models import ChatHuggingFace
from langchain_community.llms.huggingface_endpoint import HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate

token = os.environ['HF_TOKEN'] # Ideally, we have this token set. Otherwise, replace with hardcoded HF token.
API_URL = os.environ['LLM_ENDPOINT']
headers = {"Authorization": "Bearer " + token}
textInput = """
<|system|>
You are a chatbot who always responds politely</s>
<|user|>
{userInput}</s>
<|assistant|>
"""

llm = HuggingFaceEndpoint(
        endpoint_url=API_URL,
        task="text2text-generation",
        model_kwargs={
            "max_new_tokens": 200
        }
    )


"""
This function is used to wake up the Language Learning Model (LLM) by sending a POST request to the API endpoint.
It uses a predefined text input to initiate the wake-up process. The response from the API is printed to the console.
"""
def llm_wakeup():
    response = requests.post(API_URL, json={
        "inputs": textInput.format(userInput="Hello, how are you?")
    }, headers=headers)
    print(response.json())


"""
This function checks the connection to the Language Learning Model (LLM) by generating a response to a predefined
greeting. This utilizes the HuggingFaceEndpoint LLM, as opposed to the llm_wakeup() function, which utilizes a direct
request to the HuggingFace API.

Returns: Response generated by the LLM.
"""
def llm_connection_check():
    return llm.generate(["Hello, how are you?"])


"""
This function classifies the relevancy of a given message to a question.
It uses a chatbot model to determine if the message properly answers the question.
The chatbot responds with "yes" if the message is relevant, and "no" otherwise. STRICTLY used
within the context of test_lab.py testing for these labs.

Parameters:
message (str): The message to be classified.
question (str): The question to which the message is supposed to respond.

Returns:
bool: True if the message is relevant (i.e., it answers the question), False otherwise.
"""
def classify_relevancy(message, question):
    prompt = ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate.from_template("You are a chatbot who determines if a given message properly answers a question by "
                              "replying 'yes' or 'no''."),
        HumanMessagePromptTemplate.from_template("Does the following message answer the question: {question}? message: {message}"
        ),
    ])

    chat_model = ChatHuggingFace(llm=llm)
    chain = prompt | chat_model | StrOutputParser()
    result = chain.invoke({"message": message, "question": question})
    print("Result: " + result)
    if "yes" in result.lower():
        if "i will respond with 'yes' or 'no'" in result.lower():
            print("Message is not relevant")
            return False
        else:
            return True
    else:
        print(message)
        return False
