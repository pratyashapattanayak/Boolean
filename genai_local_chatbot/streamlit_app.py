import streamlit as st
import requests

st.title("GenAI Local KB Chatbot")
issue = st.text_input("Describe your issue")
dry_run = st.checkbox("Dry Run Mode", value=True)

if st.button("Get Solution"):
    response = requests.post("http://localhost:5000/chat",
                             json={"issue": issue, "dry_run": dry_run}).json()
    st.subheader("Suggested Steps")
    st.code(response['steps'])
    st.subheader("LLM Summary")
    st.write(response['llm_summary'])