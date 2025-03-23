import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Hide sidebar
st.markdown(
    """
    <style>
        [data-testid="stSidebar"] {display: none;}
        .quiz-box {background-color: orange; padding: 15px; border-radius: 10px; margin-bottom: 10px;}
    </style>
    """,
    unsafe_allow_html=True
)

# Get API key
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    st.error("❌ API Key is missing. Please check your .env file.")
    st.stop()

genai.configure(api_key=gemini_api_key)

def generate_quiz(text, difficulty):
    """Generate a multiple-choice quiz using Gemini AI."""
    model = genai.GenerativeModel("gemini-2.0-flash")
    prompt = f"""
    Generate a {difficulty} level multiple-choice quiz from the following text:
    {text}
    
    Format:
    Q1: Question?
    a) Option 1
    b) Option 2
    c) Option 3
    d) Option 4
    Answer: The correct answer in the format (e.g., "b) Option 2")
    """
    response = model.generate_content([prompt])
    return response.text if response else "⚠️ Could not generate quiz. Try again."

st.title("📚 AI-Generated Quiz")



# Retrieve stored session values
if "quiz_text" not in st.session_state or not st.session_state.get("quiz_generated", False):
    if "user_text" not in st.session_state or not st.session_state["user_text"]:
        st.error("⚠️ No text found. Please go back and enter text.")
        st.stop()

    with st.spinner("⏳ Generating quiz... Please wait."):
        quiz_text = generate_quiz(st.session_state["user_text"], st.session_state["difficulty_level"])
        st.session_state.quiz_text = quiz_text
        st.session_state["quiz_generated"] = True
        st.session_state.user_answers = {}  # Reset answers

quiz_text = st.session_state.quiz_text

# Splitting the quiz into questions and answers
lines = quiz_text.strip().split("\n")
questions = []
correct_answers = {}
if "user_answers" not in st.session_state:
    st.session_state.user_answers = {i: None for i in range(len(questions))}


for i, line in enumerate(lines):
    if line.startswith("Q"):
        questions.append({"question": line, "options": []})
    elif line.startswith(("a)", "b)", "c)", "d)")):
        if questions:
            questions[-1]["options"].append(line)
    elif line.startswith("Answer:") and questions:
        correct_answers[len(questions) - 1] = line.replace("Answer:", "").strip()

if not questions:
    st.error("⚠️ Quiz generation failed. Please try again.")
    st.stop()

# Initialize session state tracking
# if "user_answers" not in st.session_state:
#     st.session_state.user_answers = {i: None for i in range(len(questions))}

def update_answer():
    st.session_state.submitted = False  # Reset submitted status on answer change

for i, q in enumerate(questions):
    st.markdown(f'<div class="quiz-box">{q["question"]}</div>', unsafe_allow_html=True)
    selected_answer = st.session_state.user_answers.get(i, None)
    default_index = q["options"].index(selected_answer) if selected_answer in q["options"] else None

    st.session_state.user_answers[i] = st.radio(
        f"Select an answer for Q{i+1}:",
        q["options"],
        index=default_index,
        key=f"q_{i}",
        on_change=update_answer
    )


if st.button("Submit Answers"):
    st.session_state.submitted = True
    st.rerun()

if st.session_state.get("submitted", False):
    score = 0
    total_questions = len(st.session_state.user_answers)

    st.subheader("📊 Quiz Results:")
    for i in range(total_questions):
        correct = correct_answers.get(i, "")
        user_answer = st.session_state.user_answers.get(i, "")

        if not user_answer:
            st.markdown(f"⚠️ Q{i+1}: Not answered")
        elif user_answer == correct:
            score += 1
            st.markdown(f"✅ Q{i+1}: Correct! ({correct})")
        else:
            st.markdown(f"❌ Q{i+1}: Incorrect! (Correct: {correct})")

    st.markdown(f"""
        <div class="quiz-box" style="text-align: center;">
            <h3>Your Score: {score}/{total_questions}</h3>
        </div>
    """, unsafe_allow_html=True)
