# from langchain_openai import ChatOpenAI
# from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import StrOutputParser
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

# parser=StrOutputParser()
# chain=template1 | llm | parser | template2 | llm | parser 
# result=chain.invoke()

# print(result)


from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv
from langchain.output_parsers import StructuredOutputParser,ResponseSchema

import os

# Load .env
load_dotenv()
model=ChatOpenAI()

# parser=JsonOutputParser()

schema=[
    ResponseSchema(name="fact_1",description="Fact 1 about the topic"),
    ResponseSchema(name="fact_2",description="Fact 2 about the topic"),
    ResponseSchema(name="fact_3",description="Fact 3 about the topic")
]

parser=StructuredOutputParser.from_response_schemas(schema)
# Prompt templates
template1 = PromptTemplate(
    input_variables=["name"],
    template="Give me 3 record about the cricket player  {name}.\n" \
    "{format_instruction}",
    partial_variables={'format_instruction':parser.get_format_instructions()}
)


chain=template1 | model | parser

print(chain.invoke({'name':"Rohit Sharma"}))



# # Run
# prompt=template1.format(name="virat Kohli")
# result = model.invoke(prompt)
# print("\n🔍 Final Output:\n", parser.parse(result.content))
