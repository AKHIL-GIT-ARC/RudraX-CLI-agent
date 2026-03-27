import os
import tempfile
import numpy as np
import sounddevice as sd
import soundfile as sf
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SAMPLE_RATE = 16000
DURATION    = 8        # max seconds to record

def listen():
    print("Listening... speak now! (recording for up to 8 seconds)")
    print("Press Ctrl+C to stop early and process what you said.")

    try:
        # Record audio from mic
        audio = sd.rec(
            int(DURATION * SAMPLE_RATE),
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype="float32"
        )
        sd.wait()  # wait until recording is done

        # Save to a temp .wav file
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
            tmp_path = tmp.name
            sf.write(tmp_path, audio, SAMPLE_RATE)

        print("Processing your voice...")

        # Send to Groq Whisper
        with open(tmp_path, "rb") as audio_file:
            transcription = client.audio.transcriptions.create(
                file=audio_file,
                model="whisper-large-v3-turbo",
                language="en",
                response_format="text",
                temperature=0.0
            )

        os.unlink(tmp_path)  # delete temp file

        text = transcription.strip()
        if text:
            print(f"You said: {text}")
            return text
        else:
            return "I didn't catch that. Please try again."

    except KeyboardInterrupt:
        # User pressed Ctrl+C to stop recording early
        sd.stop()
        print("\nStopped early, processing...")
        return listen()

    except Exception as e:
        return f"Voice error: {str(e)}"