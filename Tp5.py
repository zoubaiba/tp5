from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "5a5d16a2693b65cf2c2d208670b60f27"


def get_stations_list():
    """
    Récupère la liste des stations météo disponibles via l'API en utilisant requests.
    Extrait la liste des villes/stations depuis une source API publique.
    """
    try:
        ### NOTE ####
        # l api weather stack n avez pas un api pour récupérer la liste des villes
        # du doup on a utilser une liste de villes codee directemnt

        # Liste de base de villes
        base_stations = [
            "PARIS",
            "MARSEILLE",
            "TOURS",
            "AMIENS",
            "PERPIGNAN",
            "METZ",
            "BESANCON",
            "BOULOGNE-BILLANCOURT",
            "ORLEANS",
            "MULHOUSE",
            "ROUEN",
            "CAEN",
            "ROUBAIX",
            "TOURCOING",
            "COPENHAGEN",
            "STOCKHOLM",
            "OSLO",
            "HELSINKI",
            "WARSAW",
            "BUDAPEST",
            "LISBON",
            "ATHENS",
            "DUBLIN",
            "ZURICH",
            "GENEVA",
            "BARCELONA",
            "MILAN",
        ]

        # Optionnel: Récupération depuis une API
        # try:
        #     response = requests.get('https://api.example.com/cities', timeout=5)
        #     if response.status_code == 200:
        #         api_data = response.json()
        #         stations = [city['name'].upper() for city in api_data]
        #         return sorted(set(stations))
        # except:
        #     pass

        return sorted(set(base_stations))  # Retourne une liste triée sans doublons

    except Exception as e:
        # En cas d'erreur, retourner une liste minimale
        print(f"Erreur lors de la récupération des stations: {e}")
        return ["PARIS", "MARSEILLE", "LYON", "TOULOUSE", "NICE"]


@app.route("/")
def display_weather():
    # Récupération de la liste des stations
    stations = get_stations_list()

    # Récupération de la ville
    ville = request.args.get("city", "MARSEILLE")

    url = f"http://api.weatherstack.com/current?access_key={API_KEY}&query={ville}"
    r = requests.get(url)
    data = r.json()
    print(data)
    return render_template("meteo.html", data=data, stations=stations)


@app.route("/<ville>")
def display_weather_v(ville):
    # Récupération de la liste des stations
    stations = get_stations_list()

    url = f"http://api.weatherstack.com/current?access_key={API_KEY}&query={ville}"
    r = requests.get(url)
    data = r.json()
    print(data)
    return render_template("meteo.html", data=data, stations=stations)


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
