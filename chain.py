# from langchain_openai import ChatOpenAI
# from langchain_core.prompts import PromptTemplate
# from dotenv import load_dotenv
# from langchain_core.output_parsers import StrOutputParser
# import os

# # Load API key from .env
# load_dotenv()

# # Initialize LLM
# llm = ChatOpenAI()

# prompt = PromptTemplate(
#     input_variables=["name"],
#         template="Give me 3 record about the cricket player  {name}."
#     )

# parser=StrOutputParser()
# chain=prompt | llm | parser

# result=chain.invoke({'name':'Pujara'})
# # print(result)
# chain.get_graph().print_ascii()



# from langchain_openai import ChatOpenAI
# from langchain_core.prompts import PromptTemplate
# from dotenv import load_dotenv
# from langchain_core.output_parsers import StrOutputParser
# import os

# Load API key from .env
# load_dotenv()

# Initialize LLM
# llm = ChatOpenAI()

# prompt1 = PromptTemplate(
#     input_variables=["name"],
#     template="Give me full info  about the cricket player  {name}."
#     )

# prompt2 = PromptTemplate(
#     input_variables=["text"],
#     template="Give me a brief 5 point summary about this following text \n  {text}."
#     )
# parser=StrOutputParser()
# chain=prompt1 | llm | parser | prompt2 | llm | parser

# result=chain.invoke({'name':'jayasuriya'})
# print(result)
# chain.get_graph().print_ascii()


# from dotenv import load_dotenv
# import os
# from langchain_openai import ChatOpenAI
# from langchain_huggingface import ChatHuggingFace
# from langchain_community.llms import HuggingFaceHub
# from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import StrOutputParser

# # Load API keys
# load_dotenv()

# # Initialize OpenAI chat model
# llm_openai = ChatOpenAI()

# # Initialize HuggingFaceHub model
# hf_llm = HuggingFaceHub(
#     repo_id="HuggingFaceH4/zephyr-7b-beta",
#     huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
#     model_kwargs={"temperature": 0.5, "max_new_tokens": 256}
# )



# # Prompt to get cricket player info
# prompt_player = PromptTemplate(
#     input_variables=["name"],
#     template="Give me full info about the cricket player {name}."
# )

# # Prompt to summarize the text
# prompt_summary = PromptTemplate(
#     input_variables=["text"],
#     template="Give me a brief 5-point summary about this following text:\n{text}"
# )

# # Output parser
# parser = StrOutputParser()

# # Chain 1: Get player info using OpenAI
# chain = prompt_player | llm_openai | parser | prompt_summary | hf_llm | parser

# # Use chain1 output to create input for chain2
# player_info = chain.invoke({"name": "jayasuriya"})

# # print(player_info)
# chain.get_graph().print_ascii()




from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_huggingface import ChatHuggingFace
from langchain_community.llms import HuggingFaceHub
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel
# from langchain.chat_models import ChatTogether
# from langchain_community.chat_models import ChatTogether
from langchain_together import ChatTogether

# Load API keys
load_dotenv()

# Initialize OpenAI chat model
llm_openai = ChatOpenAI()

# Initialize HuggingFaceHub model
# hf_llm = HuggingFaceHub(
#     repo_id="HuggingFaceH4/zephyr-7b-beta",
#     huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
#     model_kwargs={"temperature": 0.5, "max_new_tokens": 256}
# )

hf_llm = ChatTogether(
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",  # you can try other Together models
    temperature=0.7,
    max_tokens=512
)



# Prompt to get cricket player info
prompt1 = PromptTemplate(
    input_variables=["text"],
    template="Give me full info about the topic {text}."
)

# Prompt to summarize the text
prompt2 = PromptTemplate(
    input_variables=["text"],
    template="Give me 20 mcq question an option  about this following text:\n{text}"
)

prompt3 = PromptTemplate(
    input_variables=["notes","quiz"],
    template="merge both file response in single document :\n{notes} and \n {quiz}"
)

# Output parser
parser = StrOutputParser()

# Chain 1: Get player info using OpenAI
parallel_chain=RunnableParallel({
    'notes':prompt1 | llm_openai | parser,
    'quiz':prompt2 | llm_openai | parser
})
# Use chain1 output to create input for chain2

merge_chain=prompt3 | llm_openai | parser

chain=parallel_chain | merge_chain
result = chain.invoke({"text": """Artificial intelligence (AI) refers to the ability of computers to perform tasks that typically require human intelligence, such as learning, problem-solving, and decision-making. It's a field of computer science that focuses on creating systems that can simulate human cognitive abilities. AI systems are designed to learn from data, identify patterns, and make predictions or take actions based on the information they have processed. 
Here's a more detailed breakdown:
Definition:
AI is essentially the simulation of human intelligence by machines. 
Goal:
The goal of AI is to develop intelligent systems that can perform complex tasks that humans can do, like learning, reasoning, and problem-solving. 
How it works:
AI systems use algorithms, data, and computational power to simulate human intelligence. They can learn from data, identify patterns, and make predictions or decisions based on that data. 
Examples:
AI is used in various applications, including voice assistants (Siri, Alexa), self-driving cars, image recognition programs, and virtual assistants. 
Applications:
AI has a wide range of applications across different industries, including healthcare, finance, e-commerce, and transportation. 
Future:
AI is a rapidly evolving field with the potential to revolutionize many aspects of society. """})

print(result)
# chain.get_graph().print_ascii()
# chain.get_graph().print_ascii()