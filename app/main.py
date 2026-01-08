import os
import requests

BASE_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")

    if not api_key:
        print("ERROR: API_KEY is not set")
        return

    params = {
        "key": api_key,
        "q": CITY,
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    temperature = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(f"Paris weather: {temperature} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
