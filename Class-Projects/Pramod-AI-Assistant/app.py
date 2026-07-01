import os
import streamlit as st
from google import genai
from dotenv import load_dotenv

load_dotenv()

# ----------------------------
# Gemini API
# ----------------------------
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)
# ----------------------------
# Your Resume Data
# ----------------------------
my_data = """
Your Resume Data Here
"""

# ----------------------------
# Page Settings
# ----------------------------
st.set_page_config(
    page_title="Pramod AI Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Pramod AI Resume Assistant")
st.write("Ask me anything about Mukund or any general question.")

# ----------------------------
# Chat History
# ----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show old messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ----------------------------
# User Input
# ----------------------------
question = st.chat_input("Type your question...")

if question:
    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.markdown(question)

    prompt = f"""
You are Pramod Kumar's AI Assistant.

Rules:
1. Answer using the resume if possible.
2. Otherwise answer using general knowledge.
3. Keep answers simple.

Resume:
{my_data}

Question:
{question}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        answer = response.text

    except Exception as e:
        answer = f"Error: {e}"

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

    with st.chat_message("assistant"):
        st.markdown(answer)