# app.py
from flask import Flask, request, jsonify
import joblib  # or pickle
import re

app = Flask(__name__)
model = joblib.load("phishing_model.pkl")  # Load your trained model
vectorizer = joblib.load("vectorizer.pkl")  # Your vectorizer for the URL

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    url = data.get("url", "")
    if not url:
        return jsonify({"error": "URL is required"}), 400

    url_features = vectorizer.transform([url])
    prediction = model.predict(url_features)[0]

    result = "phishing" if prediction == 1 else "legitimate"
    return jsonify({"result": result})

