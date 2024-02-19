from langchain.agents import ConversationalChatAgent, AgentExecutor, create_react_agent
from tools.vectordb_tool import get_vectordb_tool
from model import get_chat_model
from agent_chat_memory import get_memory
from sales_agent_prompt import sales_agent_prompt
from langchain.agents import load_tools
from model import get_llm
from tools.general_tool import get_general_tool


# creating tools for sales agent
def get_tools():
    tools = load_tools([], llm = get_llm('openai'))
    tools.append(get_vectordb_tool())
    tools.append(get_general_tool())
    return tools



model = get_chat_model('openai')
memory = get_memory()
prefix = sales_agent_prompt
# chain = prompt | model
agent_definition = ConversationalChatAgent.from_llm_and_tools(
    llm = model,
    tools  = get_tools(),
    verbose =True,
    system_message = sales_agent_prompt,

)
agent_execution = AgentExecutor.from_agent_and_tools(
    agent=agent_definition,
    llm=model,
    tools= get_tools(),
    verbose = True,
    max_iterations=3,
    memory = memory,
    handle_parsing_erros= True

)

