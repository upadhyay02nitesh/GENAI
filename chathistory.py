from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI(
    model="gpt-4",
    temperature=0.1,
    max_completion_tokens=1000
)
chat_template = ChatPromptTemplate([
    ("system", "You are a helpful assistant that can answer questions and provide explanations."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", '{query}')

])

chat_history=[]
with open("talk.txt", "r") as file:
    chat_history.extend(file.readlines())

print(chat_history)

prompt = chat_template.format_prompt(
    query="are you send the email?",
    chat_history=chat_history
)
result=model.invoke(prompt)
print(result.content)