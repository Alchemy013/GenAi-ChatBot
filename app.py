import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash-exp")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

st.set_page_config(
    page_title="LLM Q&A",
    page_icon="👾",
    layout="wide"
)

st.title("👾 LLM Chat Application")

st.subheader("Chat History")
for message in st.session_state.chat_history:
    role, text = message
    with st.chat_message(role):
        st.markdown(f"**{role}:** {text}")

if prompt := st.chat_input("Enter your question here..."):
    with st.chat_message("user"):
        st.markdown(f"**You:** {prompt}")

    with st.spinner("Generating response..."):
        response_chunks = get_gemini_response(prompt)
        ai_response = ""
        for chunk in response_chunks:
            ai_response += chunk.text  

    with st.chat_message("assistant"):
        st.markdown(f"**Bot:** {ai_response}")

    st.session_state.chat_history.append(("user", prompt))
    st.session_state.chat_history.append(("assistant", ai_response))
