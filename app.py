import streamlit as st
import requests
import json

# Constants for the API
LLM_API_URL = "https://kanan-m49gpffn-swedencentral.cognitiveservices.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2024-08-01-preview"
LLM_API_KEY = "df9D3simI5RalfedvfQBPnuUg1PLTZcQuTStmUpu8BQ0EynYFAaLJQQJ99ALACfhMk5XJ3w3AAAAACOG4lEB"

def get_response(user_query):
    headers = {
        "Content-Type": "application/json",
        "api-key": LLM_API_KEY
    }
    
    # Prepare the message payload
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_query}
    ]
    
    payload = {
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": 150
    }
    
    # Make the API request
    response = requests.post(LLM_API_URL, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 200:
        response_data = response.json()
        return response_data["choices"][0]["message"]["content"]
    else:
        return "Error: Unable to get response from the API."

# Streamlit application
st.title("Q&A Chatbot")
st.write("Ask me anything! Type your question below:")

# User input
user_input = st.text_input("You:", "")

if st.button("Submit"):
    if user_input:
        # Get the response from the chatbot
        bot_response = get_response(user_input)
        
        # Display the bot's response
        st.write("**Bot:**", bot_response)
    else:
        st.write("Please enter a question.")
