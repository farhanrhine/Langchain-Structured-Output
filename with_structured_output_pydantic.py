# THIS CODE CAN GIVE SUMMARY OF ANY PRODUCT REVIEW IN A STRUCTURED FORMAT using pydantic, its more accurate compared to typeddict.

from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from typing import Optional, Literal
from pydantic import BaseModel, Field

load_dotenv()

model = ChatOllama(model="tinydolphin")

# schema
class Review(BaseModel):
    
    title: str = Field(description="Write the title of the review Product")
    key_themes: list[str] = Field(description="Write down all the key themes discussed in the review in a list")
    summary: str = Field(description="A brief summary of the review")
    sentiment: Literal["pos", "neg"] = Field(description="Return sentiment of the review either negative, positive or neutral")
    pros: Optional[list[str]] = Field(default=None, description="Write down all the pros inside a list")
    cons: Optional[list[str]] = Field(default=None, description="Write down all the cons inside a list")
    name: str = Field(description="Extract the name of the reviewer from the text, which should appear after 'Review by' or similar phrases. Do not use your own name.")
    

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it's an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung's One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by Farhan
""")


# print(result)
print("Structured Output:")
print("=" * 60)
print(f"\nTitle: {result.title}")
print(f"\nKey Themes: {result.key_themes}")
print(f"\nSummary: {result.summary}")
print(f"\nSentiment: {result.sentiment}")
print(f"\nPros: {result.pros}")
print(f"\nCons: {result.cons}")
print(f"\nname: {result.name}")
print("=" * 60)