import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Hide sidebar
st.markdown(
    """
    <style>
        [data-testid="stSidebar"] {display: none;}
    </style>
    """,
    unsafe_allow_html=True
)

# Load custom CSS
with open("design.css") as source_des:
    st.markdown(f"<style>{source_des.read()}</style>", unsafe_allow_html=True)

# st.title("📜 AI Quiz Generator")

# Input for text
text_input = st.text_area("📜 Enter your text here:", height=200, help="Paste any topic or passage to generate a quiz.")
st.session_state["user_text"] = text_input

# Select difficulty level
difficulty = st.selectbox("🎯 Select Quiz Difficulty:", ["Easy", "Medium", "Hard"])
st.session_state["difficulty_level"] = difficulty



# Button to generate quiz
if st.button("🚀 Generate Quiz"):
    if text_input.strip():  # Ensure text input is not empty
        st.session_state["quiz_generated"] = False  # Reset quiz state before generation
        st.switch_page("pages/the_quiz_and_result.py")
    else:
        st.warning("⚠️ Please enter text before generating the quiz.")

st.write("💡 Powered by **Google Gemini AI** | Developed with ❤️ using Streamlit")
