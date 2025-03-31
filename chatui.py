import streamlit as st
import requests


API_URL = "http://127.0.0.1:5000/chat"

st.title("🤖 Smart AI Chatbot")


if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    role = "👤 You" if message["role"] == "user" else "🤖 AI"
    st.markdown(f"**{role}:** {message['content']}")


user_input = st.text_input("Type your message:", key="input")

if st.button("Send") and user_input:
    response = requests.post(API_URL, json={"message": user_input})

    if response.status_code == 200:
        reply = response.json()["reply"]

        
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.session_state.messages.append({"role": "assistant", "content": reply})

        
        st.experimental_rerun()
    else:
        st.error("Error: Could not connect to chatbot API.")
