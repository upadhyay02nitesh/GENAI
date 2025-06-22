from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4",temperature=0.1,max_completion_tokens=1000)

chat_history = [SystemMessage(content="You are a helpful assistant that can" \
" answer questions and provide explanations.")]
while True:
    user_input=input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input=='exit':
        break
    result=llm.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print('AI: ',result.content)
print(chat_history)