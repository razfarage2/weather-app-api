import requests
from creds import api_key
from flask import Blueprint, request, jsonify



weather_bp = Blueprint("weather", __name__)  # <-- used for routing flask rest-api

@weather_bp.route("/weather/<user_input>", methods=["GET"])
def get_weather(user_input):
    weather_data = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&appid={api_key}'
    )
    if weather_data.json()['cod'] == '404':
        return jsonify({"error": "City not found"}), 404

    else:
        try:
            data = weather_data.json()
            weather = data['weather'][0]['main']
            temp = round(weather_data.json()['main']['temp'])
            return jsonify({"conditions": weather, "temp": temp})

        except Exception as e:
            return jsonify({"error": str(e)}), 500

        finally:
            print(f"The weather in {user_input} is: {weather}")
            print(f"The temp in {user_input} is: {temp}")


