from flask import Flask, render_template, request
import requests

app = Flask(__name__)  # Corrected _name to _name_
api_key = "31895d271571d8b36da9d91f08d14d86"  # Removed leading space from API key

@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None
    error_message = None

    if request.method == "POST":
        city = request.form.get("city").strip()
        url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city,
            "appid": api_key,
            "units": "metric"
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            print(data)

            weather_data = {
                "city": data["name"],
                "country": data["sys"]["country"],
                "temp": data["main"]["temp"],
                "feel_like": data["main"]["feels_like"],
                "humidity": data["main"]["humidity"],
                "condition": data["weather"][0]["description"],
                "wind_speed": data["wind"]["speed"],
            }
        except:
            error_message = "Error: Unable to fetch weather data. Please check the city name."

    return render_template("index.html", weather=weather_data, error=error_message)

if __name__ == "__main__":
    app.run(debug=True)