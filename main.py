import os
import sys
os.environ["PYTHONWARNINGS"] = "ignore"
stderr = sys.stderr
sys.stderr = open(os.devnull, 'w')

from dotenv import load_dotenv
load_dotenv()

from modules.app_launcher import open_app
from modules.search import search
from modules.datetime_util import get_time, get_date
from modules.weather import get_weather
from modules.ai_chat import chat
from modules.vision_solver import solve_from_image
from modules.problem_solver import solve

def extract_city(cmd):
    # Handles: "weather in Rajkot", "Rajkot weather",
    # "what's the weather in Rajkot now", "weather Rajkot"
    import re
    patterns = [
        r"weather\s+in\s+([a-zA-Z\s]+?)(?:\s+now|\s+today|$)",
        r"weather\s+(?:of\s+)?([a-zA-Z\s]+?)(?:\s+now|\s+today|$)",
        r"([a-zA-Z\s]+?)\s+weather",
    ]
    for pattern in patterns:
        match = re.search(pattern, cmd.strip(), re.IGNORECASE)
        if match:
            city = match.group(1).strip()
            # Remove filler words Whisper sometimes adds
            for filler in ["the", "a", "an", "please", "now", "today", "current"]:
                city = re.sub(rf"\b{filler}\b", "", city, flags=re.IGNORECASE).strip()
            if city:
                return city
    return "Rajkot"  # default

def process_command(command):
    cmd = command.lower().strip()

    # Exit check — catch any variation Whisper might produce
    exit_words = ["exit", "quit", "bye", "goodbye", "stop", "close"]
    if any(word in cmd for word in exit_words):
        return "__EXIT__"

    if "time" in cmd:
        return get_time()
    elif "date" in cmd:
        return get_date()
    elif cmd.startswith("open "):
        return open_app(cmd.replace("open ", "").strip())
    elif cmd.startswith("search "):
        return google_search(cmd.replace("search ", "").strip())
    elif "weather" in cmd:
        city = extract_city(cmd)
        return get_weather(city)
    elif cmd.startswith("solve image "):
        parts = cmd.replace("solve image ", "").split(" ask ")
        path = parts[0].strip()
        question = parts[1].strip() if len(parts) > 1 else "Solve this."
        return solve_from_image(path, question)
    elif cmd.startswith("solve "):
        return solve(cmd.replace("solve ", "").strip())
    else:
        return chat(command)

def main():
    print("RudraX is online! Type 'exit' to quit.\n")
    use_voice = input("Use voice input? (y/n): ").lower() == "y"

    while True:
        if use_voice:
            from modules.voice_input import listen
            command = listen()
        else:
            command = input("You: ").strip()

        if not command:
            continue

        response = process_command(command)

        # Handle exit from both voice and text
        if response == "__EXIT__":
            print("RudraX: Goodbye!")
            break

        print(f"\nRudraX: {response}\n")

if __name__ == "__main__":
    main()