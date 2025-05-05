import pyttsx3

def text_to_speech(text, output_path=None, intro=None, outro=None):
    """
    Convert text to speech using pyttsx3 (offline TTS).
    Optionally adds an intro and outro line to the speech.
    :param text: Main message to speak.
    :param output_path: Not used in pyttsx3 but kept for compatibility.
    :param intro: Optional text to speak before the main message.
    :param outro: Optional text to speak after the main message.
    """
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 160)      # Adjust speed
        engine.setProperty('volume', 1.0)    # Set volume

        # Optional: Choose a different voice (example: female voice on Windows)
        voices = engine.getProperty('voices')
        for voice in voices:
            if "female" in voice.name.lower():
                engine.setProperty('voice', voice.id)
                break

        # Speak the full sequence
        if intro:
            engine.say(intro)
        engine.say(text)
        if outro:
            engine.say(outro)

        engine.runAndWait()
        print("✅ Text-to-speech completed.")

    except Exception as e:
        print("❌ Failed to synthesize speech.")
        print(f"Error: {e}")
