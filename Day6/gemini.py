from google import genai
from dotenv import load_dotenv
import os


load_dotenv()


api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain Python inheritance in simple words"
)

print("\nAI RESPONSE:\n")
print(response.text)
