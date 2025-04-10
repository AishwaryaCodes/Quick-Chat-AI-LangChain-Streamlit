from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser 
from langchain_community.llms import Ollama

import streamlit as st 
import os
from dotenv import load_dotenv

load_dotenv()

##Langsmith tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"] = "chatbotproject"


#Creating Chatbot
prompt=ChatPromptTemplate.from_messages(
    [
        ("system", "Your are an helpfull assistant."),
        ("user", "Question:{question}")
    ]
)

##LLM Call
llm=Ollama(model="phi")

##Chain
output_parser=StrOutputParser()
chain=prompt | llm | output_parser


#Steramlit UI
st.title("💬 Phi Quick Chat AI(LangChain)")
input_text=st.text_input("Ask me Anything")


if input_text:
    st.write(chain.invoke(
        {'question':input_text},
        config={"configurable": {"session_name": "phi-chat"}}
        ))