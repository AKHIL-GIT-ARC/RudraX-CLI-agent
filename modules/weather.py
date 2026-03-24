import requests
import os

def get_weather(city="Rajkot"):
    api_key = os.getenv("WEATHER_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        res = requests.get(url).json()
        temp = res["main"]["temp"]
        desc = res["weather"][0]["description"]
        return f"Weather in {city}: {temp}°C, {desc}"
    except:
        return "Could not fetch weather. Check your API key."
