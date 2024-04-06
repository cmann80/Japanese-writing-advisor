import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain_openai import ChatOpenAI

load_dotenv()
# openai_api_key = os.getenv("OPENAI_API_KEY")

chat = ChatOpenAI(temperature=0)



messages = [
    SystemMessage(
        content="""
        
        You are a Japanese teacher for native English speaking students. 
        When presented with Japanese text, you give advice in English about how to improve it.
        Consider grammar and vocabulary but also style and natural expressions. Be nitpicky.

        """
    ),
    HumanMessage(
        content=input("write Japanese in here: ")
    ),
]

response = chat.invoke(messages)

print(response.content)
