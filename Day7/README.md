# AI-Powered Text Summarizer CLI

# Overview

This project is a Command Line Interface (CLI) based AI-powered text summarizer built using Python and the Gemini API.

The application reads text content from a file, sends it to Gemini AI for summarization, and generates summaries in different lengths and writing styles.


# Features

* AI-powered text summarization using Gemini API
* Command-line interface using `argparse`
* Supports different summary lengths:

  * short
  * medium
  * long
* Supports different writing styles:

  * formal
  * simple
* File handling using Python
* Error handling for:

  * missing files
  * empty files
  * missing API key
  * API/network issues
* Secure API key management using .env

# Project Structure

Day7/
summarize.py
article1.txt
article2.txt
.env
.gitignore
requirements.txt
README.md

# Technologies Used

* Python
* Gemini API
* Google GenAI SDK
* VS Code



# Install Required Packages

bash :
pip install -r requirements.txt


# Setup Environment Variables

Create a .env file and add your Gemini API key:

env

GEMINI_API_KEY=your_api_key


# Run the Project

# Example 1

bash

python summarize.py article1.txt --length short --style formal


# Python Concepts

* argparse
* File handling
* Classes
* Error handling
* Environment variables
* Command-line applications


# GenAI Concepts

* Gemini API integration
* AI-powered summarization
* Prompt engineering
* Token usage


# Error Handling Implemented

The application handles:

* Missing text files
* Empty files
* Missing API key
* API request failures
* Invalid arguments


# Sample Output

SUMMARY:

Artificial Intelligence is transforming industries
through automation, improved productivity, and
advanced decision-making capabilities.

# Requirements


google-genai
python-dotenv


