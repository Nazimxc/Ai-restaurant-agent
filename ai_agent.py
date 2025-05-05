import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def generate_response(prompt):
    try:
        response = client.chat.completions.create(
            model="mistralai/mistral-7b-instruct",  # You can change model if you like
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant for booking restaurant reservations."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"AI generation error:\n\n{e}")
        return "Sorry, I had trouble generating a response."
