from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def display_weather():
    # Récupération de station passé dans l'URL
    # Si le paramètre est absent,MARSEILLEest utilisé par défaut
    station = request.args.get('station', 'MARSEILLE')
    # Création d'un dictionnaire contenant des données fictives
    donnees_fictives = {
        "ville": station,
        "temperature": 9.3,
        "Vitesse du vent": 0.9 ,
        "pluie dans la derniere heure": 0 
    }
    #transformation dictionnaire en fichier json+
    return jsonify(donnees_fictives)

if __name__ == '__main__':
    
    app.run(host='127.0.0.1', port=3000, debug=True)