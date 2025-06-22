from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI(
    model="gpt-4",
    temperature=0.1,
    max_completion_tokens=1000
)

chat_template = ChatPromptTemplate([
    ("system", "You are a expert in '{domain}' and can answer questions related to it. "),
    ("human", "Answer the following question: '{question}' "),
    ("ai", "Provide a detailed explanation and answer the question.")
])

prompt = chat_template.format_prompt(
    domain="AI and Machine Learning",   # Example domain
    question="What is the difference between supervised and unsupervised learning?"
)
print(prompt)                                                                                                                                       