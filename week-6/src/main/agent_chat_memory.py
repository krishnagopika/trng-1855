from langchain.memory import ConversationBufferWindowMemory
from datetime import datetime
import os
from langchain_community.chat_message_histories import SQLChatMessageHistory

# chat_history_messages = SQLChatMessageHistory(session_id=datetime.now().strftime("%m/%d/%Y, %H:%M"), connection_string=os.getenv('CHAT_SQL_CONNECTION_URL'))

def get_memory():
    return ConversationBufferWindowMemory(k=3, memory_key='chat_history', return_messages=True)
