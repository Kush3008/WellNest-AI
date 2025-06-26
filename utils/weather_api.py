# utils/weather_api.py
import requests
import os

def get_weather(city):
    api_key = os.getenv("WEATHER_API_KEY")
    if not api_key:
        return "Weather info unavailable (API key missing)."

    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            return f"Weather info not available for {city}"

        condition = data['weather'][0]['description']
        temp = data['main']['temp']
        return f"{condition} with {temp:.1f}°C in {city}"

    except Exception as e:
        return f"Error fetching weather: {e}"

