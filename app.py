from flask import Flask, render_template, request
import requests
from geopy.geocoders import Nominatim
import socket

app = Flask(__name__)

API_KEY = "ea3a2779b367fbb09411e12c61031c50"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    return response.get('city')


def get_weather(city):
    request_url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(request_url)
    if response.status_code == 200:
        data = response.json()
        weather = {
            'description': data['weather'][0]['description'],
            'temp': round(data['main']['temp'], 2),
            'feels_like': round(data['main']['feels_like'], 2),
            'wind_speed': data['wind']['speed'],
            'humidity': data['main']['humidity'],
            'visibility': data['visibility'] / 1000,  # Convert to km
            'pressure': data['main']['pressure'],
            'dew_point': data['main']['dew_point'] if 'dew_point' in data['main'] else "N/A",
            'icon': data['weather'][0]['icon'],
            'city': data['name'],
            'country': data['sys']['country'],
            'time': data['dt']
        }
        return weather
    else:
        return None


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    weather = get_weather(city)
    if weather:
        return render_template('index.html', weather=weather, error=None)
    else:
        error = "Error: Unable to fetch weather data. Please check the city name and try again."
        return render_template('index.html', error=error, weather=None)


@app.route('/current_location_weather')
def current_location_weather():
    city = get_location()
    weather = get_weather(city)
    if weather:
        return render_template('index.html', weather=weather, error=None)
    else:
        error = "Error: Unable to fetch weather data for your current location."
        return render_template('index.html', error=error, weather=None)


if __name__ == '__main__':
    app.run(debug=True)
