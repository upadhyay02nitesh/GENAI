from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize the model
chat = ChatOpenAI(model="gpt-4",temperature=0.1,max_completion_tokens=10)

# Create user message
# message = "What is the capital of France?"
message = "suggest a best poem?"

# Use the recommended `invoke()` method
response = chat.invoke(message)

# Print the result
# print(response)
print(response.content)  # Assuming response is a message object with content attribute
