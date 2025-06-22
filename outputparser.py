from typing import TypedDict,Annotated,Optional,Literal
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI(
    model="gpt-4",
    temperature=0.1,
    max_completion_tokens=1000
)

# class Review(TypedDict):
#     summary: str
#     sentiment: str


class Review(TypedDict):
    summary: Annotated[str,'A brief summary of the review.']
    sentiment: Annotated[Literal["pos",'neg'],'The overall sentiment of the review, such as "positive", "negative", or "neutral".']
    key_themes: Annotated[list[str],'A list of key themes or topics mentioned in the review.']
    pros:Annotated[Optional[list[str]],'A list of positive aspects mentioned in the review.']
    cons:Annotated[Optional[list[str]],'A list of negative aspects mentioned in the review.']


structured_model=model.with_structured_output(Review)

result = structured_model.invoke("""This smartwatch is sleek, lightweight, and fits comfortably on the wrist.
The battery life lasts up to 5 days, which is quite impressive.
Health tracking features like heart rate and sleep monitor are accurate.
Overall, it's a great value for the price and highly recommended!
However, the customer service is responsive and helpful.
I would rate it 4 out of 5 stars.""")


print(result)
# print("Summary:", result['summary'])
# print("Sentiment:", result['sentiment'])



