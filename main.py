import time
from utils.speech_to_text import transcribe_audio
from utils.text_to_speech import text_to_speech
from utils.record_audio import record_audio
from database import add_reservation, create_table
from utils.parse_utils import extract_number_from_text, words_to_digits
from word2number import w2n
from sms_module import send_sms
from export import export_to_excel  # Excel export


def prompt_and_listen(prompt_text, duration=5, retries=2):
    """Speak prompt, record from mic, and transcribe it."""
    for attempt in range(retries):
        print("🤖 Asking:", prompt_text)
        text_to_speech(prompt_text)

        time.sleep(1)
        record_audio(duration=duration)
        user_text = transcribe_audio("audio.wav")
        print("🗣️ You said:", user_text)

        if user_text.strip():  # If user said something
            return user_text

        # Retry message
        text_to_speech("Sorry, I didn’t get that. Can you please repeat?")
    return ""


def format_time(time_text):
    try:
        time_words = time_text.lower().split()
        hour = w2n.word_to_num(time_words[0])
        period = time_words[1].upper() if len(time_words) > 1 else "PM"
        return f"{hour} {period}"
    except:
        return time_text


def main():
    create_table()
    print("🔊 Starting AI Restaurant Agent with Mic Recording...")

    # Friendly Intro
    text_to_speech("Welcome to our restaurant booking service, powered by AI! Let’s get started.")

    name = prompt_and_listen("Hi! What is your name?")
    contact_text = prompt_and_listen("Thanks. Could you tell me your contact number?", duration=10)
    time_slot_text = prompt_and_listen("What time would you like to book the table for?")
    guests_text = prompt_and_listen("How many guests will be coming?")

    guests = extract_number_from_text(guests_text)
    contact = words_to_digits(contact_text)

    # Add +91 if missing
    if not contact.startswith("+"):
        contact = "+91" + contact

    time_slot = format_time(time_slot_text)

    confirmation = f"Thanks {name}. Your table for {guests} guests is booked at {time_slot}. We’ll contact you at {contact}."
    print("🤖 Confirmation:", confirmation)
    text_to_speech(confirmation)

    if all([name, contact, time_slot, guests]):
        if add_reservation(name, contact, time_slot, guests):
            print("✅ Reservation saved to database.")
            export_to_excel()
            sms_message = f"Hello {name}, your table for {guests} guests has been confirmed at {time_slot}. Thank you!"
            send_sms(contact, sms_message)
        else:
            print("❌ Failed to save reservation.")
    else:
        print("⚠️ Incomplete info, not saved.")

    # Friendly Outro
    text_to_speech("👍 All set! We look forward to serving you. Have a great day!")


if __name__ == "__main__":
    main()
