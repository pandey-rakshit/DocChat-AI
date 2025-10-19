import streamlit as st
from src.app import App

st.set_page_config(
    page_title='DocChat AI',
    layout='wide',
    page_icon='app/static/chatbot.png'
)

def load_custom_css():
    with open('static/custom.css') as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def main():
    load_custom_css()
    main_container = st.container()
    with main_container:
        st.title("RAG-Powered Document Chatbot")
        st.caption("An intelligent assistant that uses retrieval-augmented generation and LLMs to answer your questions directly from uploaded PDFs.")
    
    
    

if __name__ == '__main__':
    main()
    App()