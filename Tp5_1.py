from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def display_weather():
    station = request.args.get('station', 'MARSEILLE')
    
    donnees_fictives = {
        "ville": station,
        "temperature": 9.3,
        "Vitesse du vent": 0.9 ,
        "pluie dans la derniere heure": 0 
    }
    return jsonify(donnees_fictives)

if __name__ == '__main__':
    
    app.run(host='127.0.0.1', port=3000, debug=True)