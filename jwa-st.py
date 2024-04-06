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

chat = ChatOpenAI(temperature=0)

load_dotenv()

messages = [
    SystemMessage(
        content="""
        
        You are a Japanese teacher for native English speaking students. When presented with Japanese text, you give advice in English about how to improve it.
        """
    ),
    HumanMessage(
        content="私の名前がクリスです"
    ),
]
# response = chat.invoke(messages)


# Initialize session state for storing generated text if not already done
if 'generated_text' not in st.session_state:
    st.session_state.generated_text = ""

# Text area for input
input_text = st.text_area(label="Enter your prompt", height=20)



if st.button('Generate'):
    st.session_state.generated_text += chat.invoke(messages)
    st.write(st.session_state.generated_text)