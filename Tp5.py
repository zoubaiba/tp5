from flask import Flask, render_template, request
import requests 
app = Flask(__name__)

@app.route('/')
def display_weather():
    # Récupération de la ville 
    ville = request.args.get('city', 'MARSEILLE') 
    
    API_KEY = "5a5d16a2693b65cf2c2d208670b60f27"
    url = f"http://api.weatherstack.com/current?access_key={API_KEY}&query={ville}"   
    r = requests.get(url)
    data = r.json()
    print(data)
    return render_template('meteo.html', data=data)

@app.route('/<ville>')
def display_weather_v(ville):
    
    API_KEY = "5a5d16a2693b65cf2c2d208670b60f27"
    url = f"http://api.weatherstack.com/current?access_key={API_KEY}&query={ville}"   
    r = requests.get(url)
    data = r.json()
    print(data)
    return render_template('meteo.html', data=data)