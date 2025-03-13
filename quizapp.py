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


# the style I will be using

# Custom Hero Section
# st.markdown(
#     """
#     <div style="text-align: center; padding: 50px; background-color: #FFF5E1; border-radius: 10px;">
#         <h1 style="color: #E44D26; font-size: 48px; font-weight: bold;">Making a Presentation?</h1>
#         <h2 style="color: #F79F1F; font-size: 36px;">Just <b>Slide it In</b></h2>
#         <p style="color: #333; font-size: 18px;">Upload your documents and instantly get beautiful, presentation-ready slides in under 3 minutes.</p>
#         <button style="background-color: #FF9800; color: white; padding: 15px 30px; font-size: 20px; border: none; border-radius: 5px; cursor: pointer;">Upload Documents</button>
#     </div>
#     """,
#     unsafe_allow_html=True
# )

# Keep the existing quiz generator functionality

com.iframe("https://lottie.host/embed/06d984cf-78a0-40f0-a5ec-4955a96d1383/PLUuEx0KXG.lottie")
st.title("Quiz Generator")





st.write("Make your learning more engaging and start Generating quizzes from any text using **Google Gemini AI**.")
st.page_link("pages/quiz_displaying_page.py", label="Start Now", icon="🚀")


