import streamlit as st

def toggle_upload():
    print("toggle_upload")

def show_home():
    chat_input_container = st.container(key="chat-input-container")
    with chat_input_container:
        col1, col2 = st.columns([0.6, 9.4])
        with col1:
            if st.button("&#65291;", key="plus"):
                pass
        with col2:
            st.chat_input(placeholder="Type your message...", key="message_input")