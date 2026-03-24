import os
import sys
os.environ["PYTHONWARNINGS"] = "ignore"
stderr = sys.stderr
sys.stderr = open(os.devnull, 'w')

from dotenv import load_dotenv
load_dotenv()

from modules.app_launcher import open_app
from modules.search import google_search
from modules.datetime_util import get_time, get_date
from modules.weather import get_weather
from modules.ai_chat import chat
from modules.vision_solver import solve_from_image
from modules.problem_solver import solve

def process_command(command):
    cmd = command.lower().strip()

    if "time" in cmd:
        return get_time()
    elif "date" in cmd:
        return get_date()
    elif cmd.startswith("open "):
        return open_app(cmd.replace("open ", ""))
    elif cmd.startswith("search "):
        return google_search(cmd.replace("search ", ""))
    elif "weather" in cmd:
        city = cmd.replace("weather in", "").replace("weather", "").strip() or "Rajkot"
        return get_weather(city)
    elif cmd.startswith("solve image "):
        parts = cmd.replace("solve image ", "").split(" ask ")
        path = parts[0].strip()
        question = parts[1].strip() if len(parts) > 1 else "Solve this."
        return solve_from_image(path, question)
    elif cmd.startswith("solve "):
        return solve(cmd.replace("solve ", ""))
    else:
        return chat(command)

def main():
    print(" RudraX is online! Type 'exit' to quit.\n")
    use_voice = input("Use voice input? (y/n): ").lower() == "y"

    while True:
        if use_voice:
            from modules.voice_input import listen
            command = listen()
        else:
            command = input("You: ").strip()

        if not command:
            continue

        if command.lower() in ["exit", "quit", "bye"]:
            print("RudraX: Goodbye!")
            break

        response = process_command(command)
        print(f"\nRudraX: {response}\n")

if __name__ == "__main__":
    main()
