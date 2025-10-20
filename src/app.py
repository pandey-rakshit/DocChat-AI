import streamlit as st
from src.components import sidebar
from src.pages import chat, home

def App():
    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    if "active_page" not in st.session_state:
        st.session_state["active_page"] = "Home"

    st.markdown("----")
    
    page = sidebar.render_sidebar()
    if page == "Home":
        home.show_home()
    elif page == "Chat":
        chat.show_chat()
