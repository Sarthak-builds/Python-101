from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage, HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
import os
import operator
from langgraph.checkpoint.memory import InMemorySaver


load_dotenv()
api_key = os.getenv('GOOGLE_API_KEY')

model = ChatGoogleGenerativeAI(
    model = 'gemini-3.8-flash',
    api_key = api_key
)



from langgraph.graph import add_messages


class ChatState(TypedDict):

    messages: Annotated[list[BaseMessage], add_messages ]


def chat_node(state: ChatState):

    messages = state['messages']

    response = model.invoke(messages)

    return {'messages': [response]}    

checkpointer = InMemorySaver()
graph = StateGraph(ChatState)

graph.add_node('chat_node',chat_node)

graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node', END)

chatbot = graph.compile(checkpointer = checkpointer)