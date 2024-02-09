from langchain.llms.deepinfra import DeepInfra
from langchain_experimental.chat_models import Llama2Chat
from langchain_openai.chat_models import ChatOpenAI
from langchain_openai.llms import OpenAI


def get_chat_model(model:str):
    if(model == "llama2"):
        llm = DeepInfra(
        model_id="meta-llama/Llama-2-70b-chat-hf"
        )
        model = Llama2Chat(llm=llm)
    if(model=="openai"):
        model = ChatOpenAI()
    
    return model

def get_llm(llm:str):
    if(llm == "llama2"):
        llm = DeepInfra(
        model_id="meta-llama/Llama-2-70b-chat-hf"
        )
    if(llm=="openai"):
        llm = ChatOpenAI()
    
    return llm


    
