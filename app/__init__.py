from flask import Flask, render_template, request
import requests


app = Flask(__name__)
app.config['SECRET_KEY'] = 'X-Python'
open_weather_token = '1c9f5895135ee71a8a6873c31d6e2d74'


def get_weather(city):
    code_to_smile = {
        'Clear': 'clear\U00002600',
        'Clouds': 'clouds\U00002601',
        'Rain': 'rain\U00002614'
    }

    r = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric'
    )
    data = r.json()
    city = data['name']
    current_weather = data['main']['temp']
    weather_description = data['weather'][0]['main']
    if weather_description in code_to_smile:
        wd = code_to_smile[weather_description]
    else:
        wd = 'show to window😉'
    if current_weather <= 0:
        result = 'A cold, isn’t it?'
    elif 0 < current_weather < 10:
        result = 'Cool'
    else:
        result = 'Nice weather we’re having'
    end_result = [f'weather in the city: {city}', f'temperature: {current_weather}C° {wd}', f'{result}']
    return end_result


@app.route('/', methods=['POST', 'GET'])
def index():
    end_result = ['WELCOME']
    if request.method == 'POST':
        city = request.form.get('city_name')
        end_result = get_weather(city)
    return render_template('index.html', end_result=end_result)
