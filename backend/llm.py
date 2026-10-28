import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def generate_answer(question, context):

    prompt = f"""
You are an intelligent PDF assistant.

Answer ONLY using the information provided in the context.

If the user asks:
- "in 50 words" -> answer in approximately 50 words
- "in 100 words" -> answer in approximately 100 words
- "summarize" -> give a summary
- "list skills" -> give bullet points

If the answer is not present in the context, clearly say:
"I could not find that information in the uploaded PDF."

Context:
{context}

Question:
{question}

Provide a precise answer.
"""

    
    response = model.generate_content(prompt)
        
    return response.text

    