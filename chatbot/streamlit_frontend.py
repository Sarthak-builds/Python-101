import os
import uuid

import streamlit as st
from chatbot_backend import chatbot
from langchain_core.messages import HumanMessage

MAX_THREADS_SHOWN = 10


def generate_thread_id() -> str:
    return str(uuid.uuid4())


def reset_chat():
    st.session_state['thread_id'] = generate_thread_id()
    st.session_state['message_history'] = []
    st.session_state['chat_threads'].insert(0, st.session_state['thread_id'])


def add_message(role, content):
    """Append a message to the display history (rendering is handled elsewhere)."""
    st.session_state['message_history'].append({'role': role, 'content': content})


def extract_text(content):
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return ''.join(
            part.get('text', '') if isinstance(part, dict) else str(part)
            for part in content
        )
    return str(content)


if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generate_thread_id()

if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads'] = [st.session_state['thread_id']]

st.sidebar.title('LangGraph Chatbot')

if st.sidebar.button('New Chat'):
    reset_chat()

st.sidebar.header('My Conversations')
for thread_id in st.session_state['chat_threads'][:MAX_THREADS_SHOWN]:
    st.sidebar.write(thread_id[:8])

st.title('Chat')

for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.write(message['content'])

user_input = st.chat_input('Type here:')

if user_input:
    add_message('user', user_input)
    with st.chat_message('user'):
        st.write(user_input)

    config = {
        'configurable': {'thread_id': st.session_state['thread_id']},
        'metadata': {'thread_id': st.session_state['thread_id']},
        'run_name': 'chat_turn',
    }

    with st.chat_message('assistant'):
        response = chatbot.stream(
            {'messages': [HumanMessage(content=user_input)]},
            config=config,
            stream_mode='messages',
        )
        ai_message = st.write_stream(
            extract_text(chunk.content)
            for chunk, _meta in response
            if chunk.content
        )

    # the streamed reply is already on screen; only record it in history
    add_message('assistant', ai_message)
