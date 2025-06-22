from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
import os

load_dotenv()
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "your_huggingface_api_token"

# Instantiate the model
llm = HuggingFaceEndpoint(
    repo_id="google/flan-t5-small",  # ✅ use only one: repo_id
    model="google/flan-t5-small"
)
model = ChatHuggingFace(llm=llm)
result = model.invoke("Write a short and beautiful poem about nature.")
print(result.content)
