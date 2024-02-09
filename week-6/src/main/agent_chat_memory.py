from langchain.memory import ConversationBufferWindowMemory


def get_memory():
    return ConversationBufferWindowMemory(k=3, memory_key='chat_history', return_messages=True)
