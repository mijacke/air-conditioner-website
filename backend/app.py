from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to access backend

# Add a default route for testing
@app.route("/", methods=["GET"])
def home():
    return "Flask backend is running!"

# API endpoint to test frontend connection
@app.route("/api/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello from Mario Lassu!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)  # Render will use port 10000
