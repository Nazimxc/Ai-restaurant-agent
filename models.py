# model.py

import os
import openai
from dotenv import load_dotenv

load_dotenv()

# Load the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_response(user_input):
    """
    Sends the user's input to OpenAI and returns the AI-generated response.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if you have access
            messages=[
                {"role": "system", "content": "You are a helpful assistant for a restaurant. Help users with booking tables and answering questions."},
                {"role": "user", "content": user_input}
            ],
            temperature=0.7,
            max_tokens=150
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error communicating with OpenAI: {e}"
