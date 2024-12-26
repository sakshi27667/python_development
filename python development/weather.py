import requests

print("Weather Dashboard")

api_key = "31895d271571d8b36da9d91f08d14d86"
base_url = "http://api.openweathermap.org/data/2.5/weather"

while True:
    city = input("Enter city name: (or type exit for quit): ").strip()
    if city.lower() == "exit":
        break
    if not city:
        print("Please enter a valid city name")
        continue

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        feel_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        print(f"Weather in {city}, {country}:")
        print(f"Temperature: {temp}°C (feels like: {feel_like}°C)")
        print(f"Condition: {condition}")
        print(f"Humidity: {humidity}%")
        print(f"Wind speed: {wind_speed} m/s\n")

    except KeyError:
        print("Error")
