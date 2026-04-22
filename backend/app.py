from flask import Flask, send_from_directory, jsonify
from backend.dataset import city_data
from backend.utils import get_aqi_category, health_advice
import numpy as np
import joblib
import os

app = Flask(__name__)

# Load ML model
model = joblib.load("backend/model.pkl")

# Serve HTML file
@app.route("/")
def home():
    return send_from_directory("../frontend", "index.html")

# Serve CSS
@app.route("/style.css")
def style():
    return send_from_directory("../frontend", "style.css")

# Serve JavaScript
@app.route("/script.js")
def script():
    return send_from_directory("../frontend", "script.js")

# AQI API
@app.route("/get_aqi/<city>")
def get_aqi(city):

    city = city.title()

    if city not in city_data:
        return jsonify({"error": "City not found"})

    data = city_data[city]

    features = np.array([
        data["pm25"],
        data["pm10"],
        data["no2"],
        data["co"]
    ]).reshape(1, -1)

    predicted_aqi = int(model.predict(features)[0])

    category = get_aqi_category(predicted_aqi)

    advice = health_advice(predicted_aqi)

    return jsonify({
        "city": city,
        "lat": data["lat"],
        "lon": data["lon"],
        "pm25": data["pm25"],
        "pm10": data["pm10"],
        "no2": data["no2"],
        "co": data["co"],
        "aqi": predicted_aqi,
        "category": category,
        "advice": advice
    })


if __name__ == "__main__":
    app.run(debug=True)