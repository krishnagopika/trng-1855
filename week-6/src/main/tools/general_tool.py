import pinecone_index
from langchain.agents import Tool
from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage
from model import get_llm, get_chat_model



prompt = ChatPromptTemplate.from_messages([SystemMessage(content="use this tool only for questions related to brightspeed. If the question is not related to brightspeed redirect user to brightspeed.")])

chain = prompt | get_chat_model('openai')

def get_general_tool():

    tool = Tool(
        func= chain.stream,
        name="General Sales Tool",
        description="Tool to answer the general questions",
        handle_parsing_errors=True
    )

    return tool
