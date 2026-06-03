from google import genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=api_key)

# Generate response
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain Python inheritance in simple words"
)

# Print AI response
print("\nAI RESPONSE:\n")
print(response.text)

# Print token usage
print("\nTOKEN USAGE:\n")

try:
    print(response.usage_metadata)
except:
    print("Token usage not available")

