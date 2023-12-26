import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

# GOOGLE_API_KEY from .env
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# Load gemini-pro llm model
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

# Func to get rsponse from gemini llm
def response(query):
    resp = chat.send_message(query, stream=True)
    return resp

# streamlit configuration
st.set_page_config(
    page_title='Question & Answer',
    page_icon="",
    layout='centered',
    initial_sidebar_state='collapsed'
)

# streamlit header
st.header("Google Gemini LLM")
# Chat history
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# input box
input_text = st.text_input("Enter The Query", key="input")
# submit button
submit = st.button("Ask Query")

if submit and input_text:
    resp = response(input_text)
    # Add query & rsponse in session
    st.session_state['chat_history'].append(("You", input_text))

    st.subheader("BOT Response")
    for chunk in resp:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Q&A Bot", chunk.text))

st.header("Chat History")
for role, text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")

