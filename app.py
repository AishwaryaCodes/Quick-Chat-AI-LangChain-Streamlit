from langchain_community.llms import HuggingFaceHub
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser 

import streamlit as st 
import os
from dotenv import load_dotenv

load_dotenv()

# Set Hugging Face token
os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Initialize Mistral LLM
llm = HuggingFaceHub(
    repo_id="tiiuae/falcon-7b-instruct",
    model_kwargs={"temperature": 0.7, "max_new_tokens": 500}
)


##Langsmith tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
LANGCHAIN_PROJECT="chatbot-project"


#Creating Chatbot
prompt=ChatPromptTemplate.from_messages(
    [
        ("system", "Your are an helpfull assistant."),
        ("user", "Question:{question}")
    ]
)

##Chain
output_parser=StrOutputParser()
chain=prompt | llm | output_parser


#Steramlit UI
st.title("💬 Mistral 7B Chatbot (LangChain)")
input_text=st.text_input("Ask me Anything")


if input_text:
    st.write(chain.invoke({'question':input_text}))