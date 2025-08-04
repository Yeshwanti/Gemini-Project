# Install the library (only run once in terminal, not in code)
# pip install google-generativeai

import google.generativeai as genai
import os

# 🔑 Replace with your own API key from Google AI Studio
os.environ["GOOGLE_API_KEY"] = "AIzaSyBvqe0Sb-pc9fGxmr9647XZkYSAkpd9DR4"

# Configure Gemini
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Load Gemini Model
model = genai.GenerativeModel("gemini-1.5-flash")

# First single prompt interaction
user_prompt = input("Enter your prompt: ")
response = model.generate_content(user_prompt)

print("\nGemini Response:\n")
print(response.text)

print("\n🤖 Gemini Chatbot (type 'exit' to quit)\n")

# Continuous chat loop
while True:
    user_prompt = input("You: ")
    if user_prompt.lower() in ["exit", "quit"]:
        print("Chat ended.")
        break
    
    response = model.generate_content(user_prompt)
    print("Gemini:", response.text, "\n")

