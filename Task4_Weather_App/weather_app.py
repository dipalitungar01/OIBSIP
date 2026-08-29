import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

API_KEY = "407f9535026ab767e34793b10c130383"


def get_weather():
    city = input("Enter city name: ").strip()

    if not city:
        print("City name cannot be empty.")
        return

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        if response.status_code == 404:
            print("City not found.")
            return

        if response.status_code == 401:
            print("Invalid API key.")
            return

        response.raise_for_status()

        data = response.json()

        temperature_c = data["main"]["temp"]
        temperature_f = (temperature_c * 9 / 5) + 32
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        print("\n----- Weather Information -----")
        print("City:", city)
        print(f"Temperature: {temperature_c:.1f} °C")
        print(f"Temperature: {temperature_f:.1f} °F")
        print(f"Humidity: {humidity}%")
        print("Condition:", condition)
        print(f"Wind Speed: {wind_speed} m/s")

    except requests.exceptions.Timeout:
        print("Request timed out. Please try again.")

    except requests.exceptions.ConnectionError:
        print("Network connection error.")

    except requests.exceptions.RequestException:
        print("Unable to get weather information.")

    except KeyError:
        print("Unexpected data received from the weather service.")


get_weather()