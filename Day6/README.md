# Files 

bank_account.py :

Contains the parent `BankAccount` class with:

* Deposit functionality
* Withdraw functionality
* Balance checking
* Input validation
* String representation using __str__()


savings_account.py :

Contains the SavingsAccount class that inherits from BankAccount.

# Features

* Inheritance
* super() usage
* Interest calculation
* Accessing inherited methods

gemini.py :

Demonstrates the first Gemini API call using the Google GenAI SDK.

# Features

* Loads API key from .env
* Sends prompts to Gemini AI
* Prints AI-generated responses

.env :

Stores the Gemini API key securely.

.gitignore :

Prevents sensitive files such as .env from being uploaded to GitHub.



# Topics Covered

# Python Concepts

* Inheritance
* super()
* Method overriding
* Encapsulation conventions
* Python modules
* if __name__ == "__main__"
* Standard libraries:

  * os
  * sys
  * datetime
  * random
  * math


# GenAI Concepts

* Installing Gemini SDK
* Creating API keys using Google AI Studio
* Secure API key management using .env
* Sending prompts using Gemini API
* Generating AI responses

# Tools Used

* Python
* VS Code
* Google AI Studio
* Google GenAI SDK


