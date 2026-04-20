import os
from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

API_HOST = 'weatherapi-com.p.rapidapi.com'
API_KEY = os.getenv('WEATHERAPI_KEY')
if not API_KEY:
    raise ValueError("WEATHERAPI_KEY not set in .env")

@app.route('/', methods=['GET'])
def index():
    city = "Kolkata"
    return get_weather_template(city)

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form.get('city', '').strip()
    if not city:
        return render_template('index.html', error="Please enter a city name!", city_name="Boston")
    return get_weather_template(city)

def get_weather_template(city):
    url = "https://weatherapi-com.p.rapidapi.com/current.json"
    querystring = {"q": city}
    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": API_HOST
    }
    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()
        data = response.json()
        current = data['current']
        location = data['location']
        weather_data = {
            'city_name': f"{location['name']}, {location['country']}",
            'temp_c': current['temp_c'],
            'feel': current['feelslike_c'],
            'text': current['condition']['text'],
            'country': location['country'],
            'cloud': current['cloud'],
            'pressure': current['pressure_in'],
            'direction': current['wind_dir'],
            'wind': current['wind_mph'],
            'humidity': current['humidity'],
            'visibility': current['vis_km'],
            'last': current['last_updated']
        }
        return render_template('index.html', error=None, **weather_data)
    except Exception as e:
        return render_template('index.html', error=f"Error for {city}: {str(e)}", city_name=city)

if __name__ == '__main__':
    app.run(debug=True)
