import requests

def get_weather(city):
    api_key = "d88ae891e6e85037feecab7d95dea412"  # Replace with your actual key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()
