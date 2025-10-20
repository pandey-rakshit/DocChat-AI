import streamlit as st
from src.app import App

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title='DocChat AI',
    layout='wide',
    page_icon='static/chatbot.png'  # updated path relative to root
)


# -----------------------------
# Load custom CSS
# -----------------------------
def load_custom_css(file_path='static/custom.css'):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -----------------------------
# Theme toggle button
# -----------------------------
def theme_toggle():

    if "mode" not in st.session_state:
        st.session_state.mode = "dark"

    col1, col2 = st.columns([0.95, 0.05])
    with col2:
        if st.button("🌓"):  # simple toggle icon
            st.session_state.mode = "dark" if st.session_state.mode == "light" else "light"
# -----------------------------
# Apply theme-based CSS overrides
# -----------------------------
def apply_theme_css():
    theme = st.session_state.mode
    print(theme)
    theme = st.session_state.mode
    st.components.v1.html(f"""
    <script>
        const root = window.parent.document.querySelector('#root'); // Streamlit root div
        if(root) {{
            root.setAttribute('data-theme', '{theme}');
        }}
    </script>
    """, height=0)

# -----------------------------
# Main function
# -----------------------------
def main():
    # Load custom CSS
    load_custom_css()

    # Theme toggle
    theme_toggle()

    # Apply theme overrides
    apply_theme_css()

    # Main container with title and caption
    main_container = st.container()
    with main_container:
        st.title("RAG-Powered Document Chatbot")
        st.caption(
            "An intelligent assistant that uses retrieval-augmented generation and LLMs "
            "to answer your questions directly from uploaded PDFs."
        )

# -----------------------------
# Entry point
# -----------------------------
if __name__ == '__main__':
    main()
    App()
