from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatOpenAI(
    model="gpt-4",
    temperature=0.1,
    max_completion_tokens=1000
)

# ✅ OpenAI-compatible function schema
review_function_schema = {
    "name": "extract_review",
    "description": "Extract structured review information from customer feedback.",
    "parameters": {
        "type": "object",
        "properties": {
            "summary": {
                "type": "string",
                "description": "A brief summary of the review."
            },
            "sentiment": {
                "type": "string",
                "enum": ["positive", "negative"],
                "description": "The overall sentiment of the review."
            },
            "key_themes": {
                "type": "array",
                "items": {"type": "string"},
                "description": "A list of key themes or topics mentioned in the review."
            },
            "pros": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Positive aspects mentioned in the review."
            },
            "cons": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Negative aspects mentioned in the review."
            },
            "rating": {
                "type": "integer",
                "minimum": 4,
                "maximum": 5,
                "description": "Rating out of 5 (only 4 or 5 allowed)."
            }
        },
        "required": ["summary", "sentiment", "key_themes", "rating"]
    }
}

# ✅ Use `with_structured_output` using the function schema
structured_model = model.with_structured_output(review_function_schema)

# ✅ Test input
result = structured_model.invoke("""
This smartwatch is sleek, lightweight, and fits comfortably on the wrist.
The battery life lasts up to 5 days, which is quite impressive.
Health tracking features like heart rate and sleep monitor are accurate.
Overall, it's a great value for the price and highly recommended!
However, the customer service is responsive and helpful.
I would rate it 4 out of 5 stars.
""")

# ✅ Output
print(result)
