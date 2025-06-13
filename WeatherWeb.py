from flask import Flask, render_template, request
import requests

app = Flask(__name__,template_folder="templates", static_folder="static")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['GET','POST'])
def weather():
    city_name = request.form['city']
    API = "853b2b295943b45703731fb18e180d57"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API}&units=metric"
    data = requests.get(url).json()
    if data["cod"] == 200:
        weather_info = {
            "city": city_name.title(),
            "longitude": data['coord']['lon'],
            "latitude": data['coord']['lat'],
            "description": data['weather'][0]['description'].upper(),
            "temperature": data['main']['temp'],
            "feels_like": data['main']['feels_like'],
            "wind_speed": data['wind']['speed'],
            "humidity": data['main']['humidity'],
        }
        return render_template('weather.html', weather=weather_info, weather_icon = data['weather'][0]['icon'])
    else:
        return render_template('error.html', error = "City not Found")
     
if __name__ == '__main__':
    app.run(debug=True)