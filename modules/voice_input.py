import speech_recognition as sr

def listen():
    r = sr.Recognizer()
    r.energy_threshold = 300
    r.dynamic_energy_threshold = True
    r.pause_threshold = 1.0

    try:
        with sr.Microphone() as source:
            print("🎤 RudraX is listening... speak now!")
            r.adjust_for_ambient_noise(source, duration=1)
            print("🟢 Ready! Speak your command...")
            audio = r.listen(source, timeout=10, phrase_time_limit=8)

        print("⏳ Processing your voice...")
        text = r.recognize_google(audio)
        print(f"You said: {text}")
        return text

    except sr.WaitTimeoutError:
        return "I didn't hear anything. Please speak louder or try text input."
    except sr.UnknownValueError:
        return "Sorry, RudraX couldn't understand that. Try again."
    except sr.RequestError:
        return "Speech service unavailable. Check your internet connection."
    except Exception as e:
        return f"Voice error: {str(e)}"
