from google import genai
from dotenv import load_dotenv
import argparse
import os
import sys

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

# Check API key
if not api_key:
    print("Error: GEMINI_API_KEY not found in .env")
    sys.exit()

# Create Gemini client
client = genai.Client(api_key=api_key)

# Argument parser
parser = argparse.ArgumentParser(
    description="AI Powered Text Summarizer"
)

parser.add_argument(
    "filename",
    help="Text file to summarize"
)

parser.add_argument(
    "--length",
    choices=["short", "medium", "long"],
    default="short",
    help="Summary length"
)

parser.add_argument(
    "--style",
    choices=["formal", "simple"],
    default="simple",
    help="Summary style"
)

args = parser.parse_args()

# Read file
try:
    with open(args.filename, "r", encoding="utf-8") as file:
        content = file.read()

    # Empty file check
    if not content.strip():
        print("Error: File is empty")
        sys.exit()

except FileNotFoundError:
    print("Error: File not found")
    sys.exit()

except Exception as e:
    print("Error reading file:", e)
    sys.exit()

# Create prompt
prompt = (f"""
Summarize the following article.

Summary Length: {args.length}
Writing Style: {args.style}

Article:
{content}
""")

# Generate summary
try:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    print("\nSUMMARY:\n")
    print(response.text)

except Exception as e:
    print("Error generating summary:", e)
