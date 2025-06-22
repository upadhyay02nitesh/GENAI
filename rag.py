import os
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate

# Load environment variables
load_dotenv()

# Set Streamlit page
st.set_page_config(page_title="TCS Policy Chatbot", page_icon="📘")
st.title("🤖 TCS Policy Assistant")

# Load and process documents (only once)
@st.cache_resource
def load_data():
    loader = TextLoader("sample.txt")  # or full path
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = splitter.split_documents(docs)

    embedding_model = OpenAIEmbeddings()
    vectordb = Chroma.from_documents(chunks, embedding_model, persist_directory="chroma_db")
    return vectordb.as_retriever()

retriever = load_data()

# LLM and prompt
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

prompt = PromptTemplate(
    template="""
    You are a helpful assistant.
    Answer ONLY using the provided transcript context.
    If the context is insufficient, just say you don't know.

    Context:
    {context}

    Question:
    {question}
    """,
    input_variables=["context", "question"]
)

# Chat input
question = st.text_input("Ask about TCS policy:")
if st.button("Submit") and question:
    # Retrieve and respond
    docs = retriever.invoke(question)
    context = "\n\n".join([doc.page_content for doc in docs])
    final_prompt = prompt.format(context=context, question=question)
    response = llm.invoke(final_prompt)

    # Display answer
    st.markdown("### 💬 Answer:")
    st.write(response.content)
