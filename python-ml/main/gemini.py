from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

APIKEY = os.getenv("APIKEY")

# Create Gemini client
client = genai.Client(
    api_key=APIKEY
)

def extract_answer(question, retrieved_text):
    prompt = f"""
You are an interview information extractor.

QUESTION: {question}

Rules:
- Use ONLY information from the TEXT section.
- Do NOT invent any new facts.
- Do NOT repeat duplicate lines.
- If the TEXT contains conflicting answers from multiple interview experiences, do NOT merge them blindly.
- For conflicting information:
  1. Show the most commonly mentioned answer first.
  2. Then mention alternative answers separately as "Also reported".
- For interview rounds questions, provide:
  - Most common total number of rounds
  - Common round sequence
- If coding questions are present and relevant to the QUESTION, list them first.
- If the answer is not found, return exactly: NOT FOUND.
- Do NOT use asterisks (*), bullet points (-), numbering symbols, or bold for formatting.

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
