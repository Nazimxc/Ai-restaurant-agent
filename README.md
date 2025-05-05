🧠🎙️ AI Restaurant Booking Agent
This project is a smart voice-based assistant that helps users book tables at a restaurant using voice commands. It uses speech-to-text, AI question answering, text-to-speech, and stores booking data in a local database with optional SMS confirmation and Excel export.

📌 Features
🎤 Voice input (speech-to-text)

💬 Conversational AI responses (OpenRouter / OpenAI)

🔊 Voice replies (pyttsx3 for TTS)

🗓️ Bookings saved to SQLite database

📲 Optional SMS confirmation (Twilio)

📊 Export bookings to Excel

📛 Basic error handling and validation

🗂️ Project Structure
makefile
Copy
Edit
ai-restaurant-agent/
│
├── main.py                      # Core logic flow
├── database.py                  # SQLite DB creation + insert
├── sms_module.py                # SMS sending (optional)
├── export.py                    # Export bookings to Excel
├── requirements.txt             # Python dependencies
│
├── utils/
│   ├── ai_agent.py              # AI response using OpenRouter/OpenAI
│   ├── speech_to_text.py        # Converts speech to text
│   ├── text_to_speech.py        # Converts text to speech
│   ├── parse_utils.py           # Extract numbers from text
│   └── models.py                # (optional) for future DB schemas
💡 How It Works
Starts with an intro voice greeting.

Asks for user's name, phone number, number of guests, and booking time.

Converts audio to text, processes it using AI, and stores structured data.

Confirms the reservation by voice and optionally sends an SMS.

Saves to local database and generates an Excel file of all bookings.

🛠️ Technologies & Libraries
Library	Purpose
speech_recognition	Speech-to-text
pyttsx3	Text-to-speech
openai / openrouter	Chat-based AI replies
sqlite3	Database storage
pandas	Exporting to Excel
twilio (optional)	SMS notifications
word2number	Converting "three" → 3
re	Regex parsing for numbers/phones

▶️ How to Run
Clone the repo


git clone https://github.com/Nazimxc/Ai-restaurant-agent.git

Install dependencies


pip install -r requirements.txt
Set your .env file

OPENROUTER_API_KEY=your_api_key
TWILIO_SID=optional
TWILIO_AUTH_TOKEN=optional
Run the app

python main.py
✅ Future Enhancements
Web interface for browser-based voice input

Better natural language understanding

Admin dashboard to manage bookings

🧑‍🏫 Ideal For
AI + Voice beginners

Mini projects and hackathons

Demonstrating NLP and TTS integration

