from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)

st.header("Research Tool")
user_input = st.text_input("Enter your question")

if st.button("Summarize"):
    result = llm.invoke(user_input)  # Use the endpoint directly
    st.write(result)  # Output the result correctly


# LLM are very prompt sensitive 
# This is a static prompt and we not use it much in industries 
# But why ?? Because static prompt gives more control to the user 
