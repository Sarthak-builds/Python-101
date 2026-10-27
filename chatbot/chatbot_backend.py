import os
import sqlite3
from typing import Annotated, TypedDict

from dotenv import load_dotenv
from langchain_core.messages import BaseMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph import END, START, StateGraph, add_messages

load_dotenv()

api_key = os.getenv('GOOGLE_API_KEY')
model_name = os.getenv('GEMINI_MODEL', 'gemini-2.5-flash')
db_path = os.getenv('DB_PATH', 'chatbot.db')

model = ChatGoogleGenerativeAI(
    model=model_name,
    api_key=api_key,
)


class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


def chat_node(state: ChatState) -> dict:
    """Invoke the LLM with the conversation and return the AI reply."""
    messages = state['messages']
    response = model.invoke(messages)
    return {'messages': [response]}


conn = sqlite3.connect(database=db_path, check_same_thread=False)
checkpointer = SqliteSaver(conn)

graph = StateGraph(ChatState)

graph.add_node('chat_node', chat_node)

graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node', END)

chatbot = graph.compile(checkpointer=checkpointer)
