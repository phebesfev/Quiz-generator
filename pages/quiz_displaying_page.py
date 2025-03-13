import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
import streamlit.components.v1 as com

# Load environment variables from .env
load_dotenv()

# to hide the side bar 
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

# Get the API key from the environment
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini API Key securely
genai.configure(api_key=api_key)
def generate_quiz(text, difficulty):
    try:
        model = genai.GenerativeModel("gemini-2.0-flash")  # Updated to latest model
        prompt = f"Create a {difficulty} level quiz based on this text:\n\n{text}"
        response = model.generate_content([prompt])  # Corrected API input format
        
        # Ensure response is valid
        if response and hasattr(response, "text"):
            return response.text
        else:
            return "⚠️ No response from AI. Try again."

    except Exception as e:
        r
        
text_input = st.text_area("📜 Enter your text here:", height=200, help="Paste any topic or passage to generate a quiz.")
difficulty = st.selectbox("🎯 Select Quiz Difficulty:", ["Easy", "Medium", "Hard"])

if st.button("🚀 Generate Quiz"):
    if text_input.strip():
        with st.spinner("⏳ Generating quiz... Please wait."):
            quiz = generate_quiz(text_input, difficulty)
            st.subheader("🎓 Generated Quiz:")
            st.write(quiz)
    else:
        st.warning("⚠️ Please enter some text before generating.")

st.write("💡 Powered by **Google Gemini AI** | Developed with ❤️ using Streamlit")