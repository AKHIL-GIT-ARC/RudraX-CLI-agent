import requests

def get_weather(city="Rajkot"):
    try:
        # Step 1: Convert city name to coordinates (free, no key)
        geo = requests.get(
            f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
        ).json()

        if not geo.get("results"):
            return f"Could not find city: {city}"

        lat = geo["results"][0]["latitude"]
        lon = geo["results"][0]["longitude"]
        name = geo["results"][0]["name"]

        # Step 2: Get weather (free, no key)
        weather = requests.get(
            f"https://api.open-meteo.com/v1/forecast"
            f"?latitude={lat}&longitude={lon}"
            f"&current=temperature_2m,weathercode,windspeed_10m"
            f"&timezone=auto"
        ).json()

        current = weather["current"]
        temp = current["temperature_2m"]
        wind = current["windspeed_10m"]

        # Map weather code to description
        code = current["weathercode"]
        descriptions = {
            0: "clear sky", 1: "mainly clear", 2: "partly cloudy", 3: "overcast",
            45: "foggy", 48: "foggy", 51: "light drizzle", 61: "light rain",
            63: "moderate rain", 65: "heavy rain", 71: "light snow", 80: "rain showers",
            95: "thunderstorm"
        }
        desc = descriptions.get(code, "mixed conditions")

        return f"Weather in {name}: {temp}°C, {desc}, wind {wind} km/h"

    except Exception as e:
        return f"Could not fetch weather: {e}"