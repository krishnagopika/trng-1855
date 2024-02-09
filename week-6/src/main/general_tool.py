import pinecone_index
from langchain.agents import Tool
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from model import get_llm



prompt = PromptTemplate.from_template(template="use this tool only for questions related to brightspeed. If the question is not related to brightspeed redirect user to brightspeed.")

chain = prompt | get_llm('llama2')

def get_general_tool():

    tool = Tool(
        func= chain.stream,
        name="General Sales Tool",
        description="Tool to answer the general questions",
    )

    return tool
