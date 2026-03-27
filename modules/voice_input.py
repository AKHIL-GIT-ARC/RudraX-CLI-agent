import os
import tempfile
import numpy as np
import sounddevice as sd
import soundfile as sf
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SAMPLE_RATE = 16000
DURATION    = 8
DEVICE      = 0        # HDA Intel PCH CX11880 — your mic

def listen():
    print("Listening... speak now!")
    try:
        audio = sd.rec(
            int(DURATION * SAMPLE_RATE),
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype="float32",
            device=DEVICE
        )
        sd.wait()

        volume = np.max(np.abs(audio))
        print(f"Volume level detected: {volume:.4f}")

        if volume < 0.001:
            return "Mic picked up silence. Check if your mic is unmuted in system settings."

        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
            tmp_path = tmp.name
            sf.write(tmp_path, audio, SAMPLE_RATE)

        print("Processing with Groq Whisper...")

        with open(tmp_path, "rb") as audio_file:
            transcription = client.audio.transcriptions.create(
                file=audio_file,
                model="whisper-large-v3-turbo",
                language="en",
                response_format="text",
                temperature=0.0
            )

        os.unlink(tmp_path)

        text = transcription.strip()
        if text:
            print(f"You said: {text}")
            return text
        else:
            return "Couldn't catch that. Please try again."

    except Exception as e:
        return f"Voice error: {str(e)}"