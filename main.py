import streamlit as st
from chatbot import get_response

st.set_page_config(page_title="Law Awareness Chatbot", page_icon="⚖️")

st.title("⚖️ Law Awareness Chatbot")
st.write("Ask any legal questions, and I will help you!")

user_input = st.text_input("You:", "")

if st.button("Ask"):
    if user_input.strip():
        response = get_response(user_input)
        st.text_area("Chatbot:", response, height=200)
    else:
        st.warning("Please enter a question.")