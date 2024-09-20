from flask_cors import CORS
from flask import Flask
from main import *

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"*": {"origins": "http://localhost:5173"}})

    app.register_blueprint(weather_bp)


    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)