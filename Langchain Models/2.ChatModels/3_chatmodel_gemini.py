from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Initialize Gemini with correct model
model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

# Invoke prompt
response = model.invoke("What is the capital of India?")
print(response)
