from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from dotenv import load_dotenv
import os
from pydantic import BaseModel,Field

# Load .env
load_dotenv()
model=ChatOpenAI()

# parser=JsonOutputParser()

class Person(BaseModel):
    name:str=Field(description="Name of the person")
    age:int=Field(gt=18,description="Age of the person")
    city:str=Field(description="Name of the city of person birth place")

parser=PydanticOutputParser(pydantic_object=Person)
# Prompt templates
template1 = PromptTemplate(
    input_variables=["name"],
    template="Generate name,age,city  about the highest score cricket player  {name}.\n" \
    "{format_instruction}",
    partial_variables={'format_instruction':parser.get_format_instructions()}
)
chain=template1 | model | parser

print(chain.invoke({'name':"Rohit Sharma"}))
