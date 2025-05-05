import requests
import os
from dotenv import load_dotenv

load_dotenv()
DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")

def transcribe_audio(file_path):
    if not DEEPGRAM_API_KEY:
        print("❌ Deepgram API key not set.")
        return ""

    url = "https://api.deepgram.com/v1/listen"
    headers = {
        "Authorization": f"Token {DEEPGRAM_API_KEY}",
        "Content-Type": "audio/wav"
    }

    try:
        print(f"📤 Sending file: {file_path} to Deepgram...")

        with open(file_path, "rb") as f:
            response = requests.post(url, headers=headers, data=f)

        print(f"🔁 Deepgram responded with status: {response.status_code}")
        print(f"📨 Raw Response: {response.text}")

        if response.status_code == 200:
            return response.json()["results"]["channels"][0]["alternatives"][0]["transcript"]
        else:
            return "Failed to transcribe audio."

    except Exception as e:
        print(f"🚨 Exception during transcription: {e}")
        return "Error during transcription."
