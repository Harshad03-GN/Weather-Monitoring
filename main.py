from flask import Flask, render_template, request
import requests
from azure_blob import upload_weather_to_blob
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

API_KEY = "d88ae891e6e85037feecab7d95dea412"

def get_weather(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        return response.json()
    return None

@app.route("/", methods=["GET", "POST"])
def home():
    print("🧠 Entered home() route") 
    city = ""
    weather = None

    if request.method == "POST":
        print("🚀 POST request received")  
        city = request.form.get("city")
        print(f"🌆 City entered: {city}") 

        weather = get_weather(city)
        print("✅ Weather data fetched.") 

        if weather:
            print("✅ Weather data fetched.")
            upload_weather_to_blob(city, weather)
            print("✅ Upload function was called.")

    return render_template("index.html", city=city, weather=weather)


if __name__ == "__main__":
    app.run(debug=True)
