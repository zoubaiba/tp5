from flask import Flask, request, jsonify
import requests 
app = Flask(__name__)

API_KEY = "5a5d16a2693b65cf2c2d208670b60f27"

@app.route('/')
def display_weather():
    station = request.args.get('station', 'MARSEILLE')
    
    url_api = f"http://api.weatherstack.com/current?access_key={API_KEY}&query={station}"
    

    reponse = requests.get(url_api)
    data = reponse.json()

    # Création d'un dictionnaire contenant des données fictives
    infos = {
            "Ville": data['location']['name'],             
            "Temperature": data['current']['temperature'],    
            "Vitesse du vent": data['current']['wind_speed'],           
            "Quantite de precipitations": data['current']['precip']   
    }
    #transformation dictionnaire en fichier json+
    return jsonify(infos)
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, debug=True)