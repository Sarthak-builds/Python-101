
import streamlit as st
from chatbot_backend import chatbot
from langchain_core.messages import HumanMessage
import uuid


def generate_thread_id():
    thread_id = uuid.uuid4()
    return thread_id

def reset_chat():
    thread_id = generate_thread_id()
    st.session_state['thread_id'] = thread_id
    st.session_state['message_history'] = []

def add_message(role, content):
    st.session_state['message_history'].append({'role': role, 'content': content})
    with st.chat_message(role):
        st.write(content)


def add_thread(thread_id):
    if 'chat_threads' not in st.session_state:
        st.session_state['chat_threads'] = []
    if thread_id not in st.session_state['chat_threads']:
        st.session_state['chat_threads'].append(thread_id)


if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generate_thread_id()

add_thread(st.session_state['thread_id'])

CONFIG = {'configurable': {'thread_id': st.session_state['thread_id']},
          'metadata': {
              "thread_id": st.session_state['thread_id']
          },
          "run_name": "chat_turn"}

st.sidebar.title('LangGraph Chatbot')

if st.sidebar.button('New Chat'):
    reset_chat()

st.sidebar.header('My Conversations')
st.sidebar.write(str(st.session_state['thread_id']))

for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.write(message['content'])

def extract_text(content):
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return ''.join(
            part.get('text', '') if isinstance(part, dict) else str(part)
            for part in content
        )
    return str(content)


user_input = st.chat_input('Type Here: ')

if user_input:

    add_message('user', user_input)

    with st.chat_message('assistant'):
        response = chatbot.stream(
            {'messages': [HumanMessage(content=user_input)]},
            config=CONFIG,
            stream_mode='messages'
        )
        ai_message = st.write_stream(
            extract_text(chunk.content)
            for chunk, _meta in response
            if chunk.content
        )

    add_message('assistant', ai_message)
