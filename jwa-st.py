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

input_text = st.text_area(label="Enter your prompt", height=20)

messages = [
    SystemMessage(
        content="""
        
        You are an advanced Japanese teacher for native English speaking students. 
        When presented with Japanese text, you give advice in English about how to improve it.
        You will not rewrite the whole thing yourself; that is an impedement to learning.
        Think about grammar and vocabulary, but also consistency of style.
        Make sure the writing is all in the same level of politeness.
        There's no reason to translate anything that the user wrote to English; it's assumed that the user can read it just fine.
        
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