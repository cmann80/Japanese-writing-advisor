import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain_openai import ChatOpenAI
import streamlit as st

load_dotenv()

chat = ChatOpenAI(temperature=0)
st.title("Japanese Writing Advisor")

input_text = st.text_area(label="Enter Japanese text", height=20)

messages = [
    SystemMessage(
        content="""
        
        You are an advanced Japanese teacher for native English speaking students. 
        When presented with Japanese text, you give advice in English about how to improve it.
        Also, make a guess about what context it is being used in. A private communictaion with a friend, a business email etc.
        Do not translate anything the user wrote directly into Engish.
        Do not rewrite the whole text yourself.
        Think about grammar and vocabulary, but also consistency of style.
        Make sure the writing is all in the same level of politeness.
        Point out any part of it that could be offensive.
                
        """
    ),
    HumanMessage(
        content=input_text
    ),
]



# Initialize session state for storing generated text if not already done
if 'generated_text' not in st.session_state:
    st.session_state.generated_text = ""


if st.button('Respond'):
#    st.session_state.generated_text += chat.invoke(messages).content
    st.session_state.generated_text = chat.invoke(messages).content
    st.write(st.session_state.generated_text)