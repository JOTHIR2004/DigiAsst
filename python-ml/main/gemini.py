import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv() 

APIKEY = os.getenv("APIKEY")

# Create Gemini client
client = genai.Client(
    api_key=APIKEY  # set via environment variable
)

def extract_answer(question, retrieved_text):
    prompt = f"""
You are an information extractor.

QUESTION:
{question}

Rules:
- You MUST NOT generate new words.
- You MUST ONLY copy text from the TEXT section.
- If the answer is not found, return exactly: NOT FOUND.
- Dont repeat the same questions give as a whole questions with numbers and if there is any coding questions listed give it also
TEXT:
<<<
{retrieved_text}
>>>
"""

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )

    return response.text.strip()

