from langchain.agents import ConversationalChatAgent, AgentExecutor
import vectordb_tool
from model import get_chat_model
from agent_chat_memory import get_memory
from sales_agent_prompt import sales_agent_prompt
from langchain.agents import load_tools
from model import get_llm



def get_tools():
    tools = load_tools([], llm = get_llm('llama2'))
    tools.append(vectordb_tool.get_vectordb_tool())
    return tools

def get_agent():
    model = get_chat_model('llama2')
    memory = get_memory()
    system_message = sales_agent_prompt

    agent_definition = ConversationalChatAgent.from_llm_and_tools(
        llm = model,
        tools  = get_tools(),
        system_message = system_message
    )

    agent_execution = AgentExecutor.from_agent_and_tools(
        agent=agent_definition,
        llm=model,
        tools= get_tools(),
        handle_parsing_erros= True,
        verbose = True,
        max_iterations=3,
        memory = memory
    )
    return agent_execution



