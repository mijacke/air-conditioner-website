from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "https://air-conditioners-website.vercel.app"}})

@app.route("/", methods=["GET"])
def home():
    return "Flask backend is running!"

@app.route("/api/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello from Mario Lassu!"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=True)