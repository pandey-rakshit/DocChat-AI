import streamlit as st

def render_sidebar():
    st.sidebar.header("DocChat AI")

    if st.sidebar.button("➕ New Chat"):
        # Clear chat history when new chat is clicked
        # clear_chat_history()
        st.session_state['messages'] = []
        st.session_state['active_page'] = 'Home'
    return st.session_state.get("active_page", "Home")