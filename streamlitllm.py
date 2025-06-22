from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate,load_prompt
from dotenv import load_dotenv
import streamlit as st
import os
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Check and display result in Streamlit
st.title("API Key Checker")

if api_key:
    st.success("✅ API key loaded successfully.")
else:
    st.error("❌ API key not found. Check your .env file.")
llm = ChatOpenAI(model="gpt-4",temperature=0.1,max_completion_tokens=1000)
# st.header("Chat with LLM")
# input=st.text_input("Enter your query:", key="query_input")
# if st.button("Generate Response"):
#     llm = ChatOpenAI(model="gpt-4",temperature=0.1,max_completion_tokens=1000)
#     response = llm.invoke(input)
#     st.write(response.content)


st.title("📐 Math Problem Solver")

# User input for the problem
math_question = st.text_input("🧮 Enter your math problem:")

# Optional custom variables
difficulty = st.selectbox("Select difficulty level (optional):", ["", "Easy", "Medium", "Hard"])
explanation = st.selectbox("Do you want an explanation?", ["No", "Yes"])
style = st.selectbox("Explanation style (optional):", ["", "Beginner", "Step-by-step", "Concise", "Detailed"])
# LangChain PromptTemplate


# Pre-build optional prompt parts (always update live)
explanation_clause = "Then provide a detailed explanation." if explanation == "Yes" else ""
style_clause = f"Use a {style.lower()} style for explanation." if style else ""
difficulty_clause = f"Assume the problem is {difficulty.lower()} level." if difficulty else ""

# Prompt template
# template_text = """
# Solve this math problem: {question}

# Provide only a one-line short answer first.

# {explanation_clause}
# {style_clause}
# {difficulty_clause}
# """

# prompt = PromptTemplate(
#     template=template_text,
#     input_variables=["question", "explanation_clause", "style_clause", "difficulty_clause"]
# )

# # Build final prompt (live updated, even before Solve is clicked)
# final_prompt = prompt.format(
#     question=math_question,
#     explanation_clause=explanation_clause,
#     style_clause=style_clause,

# )

# template.save("math_problem_solver_prompt.json")

prompt = load_prompt("math_problem_solver_prompt.json")

final_prompt = prompt.format(
    question=math_question,
    explanation_clause=explanation_clause,
    style_clause=style_clause,
    difficulty_clause=difficulty_clause
)
# Handle the button
if st.button("💡 Solve"):
    if not math_question.strip():
        st.warning("Please enter a valid question.")
    else:

        # Invoke the model
        response = llm.invoke(final_prompt)

        st.markdown("### ✅ Answer:")
        st.write(response.content)