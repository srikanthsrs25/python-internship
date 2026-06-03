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
    usage = response.usage_metadata

    print("Prompt Tokens:", usage.prompt_token_count)
    print("Response Tokens:", usage.candidates_token_count)
    print("Total Tokens:", usage.total_token_count)

except:
    print("Token usage not available")

