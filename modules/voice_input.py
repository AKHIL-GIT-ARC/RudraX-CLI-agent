import os
import tempfile
import numpy as np
import sounddevice as sd
import soundfile as sf
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

DURATION = 8
DEVICE   = 0

def get_sample_rate():
    # Auto-detect what sample rate your device actually supports
    device_info = sd.query_devices(DEVICE, "input")
    rate = int(device_info["default_samplerate"])
    print(f"Using sample rate: {rate} Hz")
    return rate

def listen():
    print("Listening... speak now!")
    try:
        sample_rate = get_sample_rate()

        audio = sd.rec(
            int(DURATION * sample_rate),
            samplerate=sample_rate,
            channels=1,
            dtype="float32",
            device=DEVICE
        )
        sd.wait()

        volume = np.max(np.abs(audio))
        print(f"Volume level detected: {volume:.4f}")

        if volume < 0.001:
            return "Mic picked up silence. Check if mic is unmuted in system settings."

        # Resample to 16000Hz if needed (Whisper works best at 16k)
        if sample_rate != 16000:
            import scipy.signal as signal
            num_samples = int(len(audio) * 16000 / sample_rate)
            audio = signal.resample(audio, num_samples)
            sample_rate = 16000

        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
            tmp_path = tmp.name
            sf.write(tmp_path, audio, sample_rate)

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