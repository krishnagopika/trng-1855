import streamlit as st
from sales_agent import get_agent

st.title('BrightSpeed')
st.subheader('Sales Agent')

if 'chat' not in st.session_state:
  st.session_state['chat'] = [{
    "content": "Hi, I'm a sales agent for Brightspeed. How can I help you today?",
    "role": "ai"
  }]

user_input = st.chat_input('message:', key= "user_input")
if user_input:
  st.session_state['chat'].append({
    "content": user_input,
    "role": "user"
  })
  agent = get_agent()
  agent_response = agent.invoke({user_input})
  st.session_state['chat'].append({
    "content": agent_response['output'],
    "role": "ai"
  })
if st.session_state['chat']:
  for i in range(0, len(st.session_state['chat'])):
    user_message = st.session_state['chat'][i]
    st.chat_message(user_message["role"]).write(user_message["content"])
