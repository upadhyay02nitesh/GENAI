import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Initialize LLM
llm = ChatOpenAI(model="gpt-4", temperature=0.1, max_tokens=1000)

st.set_page_config(page_title="Styled Chatbot", page_icon="💬")
st.title("💬 GPT-4 Chat")

# CSS styling block
st.markdown("""
    <style>
    body {
        background-color: #121212;
        color: #ffffff;
    }
    .chat-box {
        padding: 12px 20px;
        margin: 10px;
        border-radius: 15px;
        max-width: 70%;
        word-wrap: break-word;
        font-size: 16px;
        line-height: 1.5;
        color: #f1f1f1;
    }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
    .user {
        background-color: #1e88e5;  /* Blue for user */
        margin-left: auto;
        text-align: right;
    }
    .ai {
        background-color: #2e2e2e;  /* Dark gray for AI */
        margin-right: auto;
        text-align: left;
    }
</style>

""", unsafe_allow_html=True)

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        SystemMessage(content="You are a helpful assistant.")
    ]

# Chat form
with st.form("chat_form"):
    user_input = st.text_input("Type your message:")
    submitted = st.form_submit_button("Send")

# On submit
if submitted and user_input:
    st.session_state.chat_history.append(HumanMessage(content=user_input))
    response = llm.invoke(st.session_state.chat_history)
    st.session_state.chat_history.append(AIMessage(content=response.content))

# Render chat history
for msg in st.session_state.chat_history:
    if isinstance(msg, HumanMessage):
        st.markdown(f'<div class="chat-box user">🧑 {msg.content}</div>', unsafe_allow_html=True)
    elif isinstance(msg, AIMessage):
        st.markdown(f'<div class="chat-box ai">🤖 {msg.content}</div>', unsafe_allow_html=True)
