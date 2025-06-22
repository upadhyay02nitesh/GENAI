from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import DatetimeOutputParser
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()

# Initialize LLM
llm = ChatOpenAI()

# 1. Create the datetime parser
parser = DatetimeOutputParser()

# 2. Create prompt template
prompt = PromptTemplate.from_template(
    "When was Rohit Sharma born?\n\n{format_instructions}",
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

# 3. Chain it together
chain = prompt | llm | parser

# 4. Invoke the chain
result = chain.invoke({})

print(result)
print(type(result))
