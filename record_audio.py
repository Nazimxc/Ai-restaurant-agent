# utils/record_audio.py

import sounddevice as sd
from scipy.io.wavfile import write

def record_audio(duration=5, filename="audio.wav", samplerate=44100):
    """
    Records audio from the microphone and saves it to a .wav file.
    :param duration: Duration to record in seconds
    :param filename: Output WAV file name
    :param samplerate: Sample rate for recording
    """
    print(f"🎙️ Recording for {duration} seconds...")
    recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()  # Wait until recording is finished
    write(filename, samplerate, recording)
    print(f"✅ Saved recording to {filename}")
    return filename
