# from langchain_openai import ChatOpenAI
# from langchain_core.prompts import PromptTemplate
# from dotenv import load_dotenv
# import os

# # Load environment variables
# load_dotenv()

# # Initialize the model
# llm = ChatOpenAI()


# # Prompt 1: Detailed report
# template1 = PromptTemplate(
#     input_variables=["topic"],
#     template="Write a detailed report on {topic}."
# )

# # Prompt 2: Summary of the text
# template2 = PromptTemplate(
#     input_variables=["text"],
#     template="Write a 5 lines summary of the following text:\n\n{text}"
# )

# # Generate prompt1
# topic = "Artificial Intelligence"
# prompt1 = template1.format(topic=topic)
# print("\n--- Generating Report ---\n")
# result = llm.invoke(prompt1)
# # print(result)

# # Generate prompt2 using result
# prompt2 = template2.format(text=result.content)
# print("\n--- Generating Summary ---\n")
# summary = llm.invoke(prompt2)
# print(summary.content)


from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize the model
llm = ChatOpenAI()


# Prompt 1: Detailed report
template1 = PromptTemplate(
    input_variables=["topic"],
    template="Write a detailed report on {topic}."
)

# Prompt 2: Summary of the text
template2 = PromptTemplate(
    input_variables=["text"],
    template="Write a 5 lines summary of the following text:\n\n{text}"
)

# Generate prompt1
# topic = "Artificial Intelligence"
# prompt1 = template1.format(topic=topic)
# print("\n--- Generating Report ---\n")
# result = llm.invoke(prompt1)
# # print(result)

# # Generate prompt2 using result
# prompt2 = template2.format(text=result.content)
# print("\n--- Generating Summary ---\n")
# summary = llm.invoke(prompt2)
# print(summary.content)
