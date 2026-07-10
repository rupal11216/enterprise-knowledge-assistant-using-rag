from rag_chain import build_chain
from dotenv import load_dotenv
import streamlit as st
import os

os.environ["TRANSFORMERS_VERBOSITY"] = "error"


load_dotenv()

SAMPLE_QUESTIONS = [
    "Why is my mobile internet so slow?",
    "My calls keep dropping — what should I do?",
    "How do I activate international roaming?",
    "Why is my bill higher than usual this month?",
    "My phone shows SIM not detected after a restart",
    "How do I enable Wi-Fi calling?",
    "I was charged for roaming but had a bundle active",
    "How do I unlock my phone for another network?",
]

# ---------------------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------------------
st.set_page_config(
    page_title="Telecom Support Assistant",
    page_icon="📡",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------------------
# Load RAG Chain
# ---------------------------------------------------------------------


@st.cache_resource
def get_chain():
    return build_chain()


# ---------------------------------------------------------------------
# Session State
# ---------------------------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "pending_question" not in st.session_state:
    st.session_state.pending_question = None


# ---------------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------------
with st.sidebar:

    st.title("📡 Telecom Support")

    st.caption("RAG-powered customer support assistant")

    st.divider()

    with st.container(border=True):

        st.markdown("### Example Questions")

        st.caption("Click any question to try the assistant.")

        for q in SAMPLE_QUESTIONS:

            if st.button(q, use_container_width=True):
                st.session_state.pending_question = q

    st.divider()

    if st.button(
        "🗑️ Clear Conversation",
        use_container_width=True,
    ):
        st.session_state.messages = []


# ---------------------------------------------------------------------
# Header
# ---------------------------------------------------------------------
st.title("Telecom Customer Care Assistant")

st.markdown(
    """
Ask questions related to:

- Network & Connectivity
- Billing & Payments
- SIM Issues
- International Roaming
- Wi-Fi Calling
- General Telecom Support
"""
)

st.divider()

# ---------------------------------------------------------------------
# Welcome Screen
# ---------------------------------------------------------------------
if not st.session_state.messages:

    st.info(
        """
### Welcome

Ask a question in natural language or select one of the sample
questions from the sidebar.

The assistant searches a telecom knowledge base before generating
each response.
"""
    )

# ---------------------------------------------------------------------
# Chat History
# ---------------------------------------------------------------------
for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):

        st.markdown(msg["content"])


# ---------------------------------------------------------------------
# User Input
# ---------------------------------------------------------------------
question = st.chat_input("Describe your telecom issue...")

if st.session_state.pending_question:
    question = st.session_state.pending_question
    st.session_state.pending_question = None


# ---------------------------------------------------------------------
# Generate Response
# ---------------------------------------------------------------------
if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question,
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("Searching knowledge base..."):

            chain = get_chain()

            response = st.write_stream(
                chain.stream(question)
            )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response,
        }
    )
