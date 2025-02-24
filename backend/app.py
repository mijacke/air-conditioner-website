from flask import Flask, jsonify
from flask_cors import CORS
import os, logging
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app, resources={r"/api/*": {"origins": app.config.get("ALLOWED_ORIGINS")}})
    logging.basicConfig(level=logging.INFO)

    @app.route("/", methods=["GET"])
    def home():
        return "Flask backend is running!"

    @app.route("/api/hello", methods=["GET"])
    def hello():
        return jsonify({"message": "Hello from Mario Lassu!"})

    @app.route('/api/services', methods=['GET'])
    def get_services():
        try:
            services = [
                {"id": 1, "name": "Sales", "description": "High-quality air conditioning units."},
                {"id": 2, "name": "Repair", "description": "Expert repair services."},
                {"id": 3, "name": "Assembly", "description": "Professional installation services."}
            ]
            return jsonify(services)
        except Exception as e:
            app.logger.error("Error retrieving services: %s", e)
            return jsonify({"error": "Internal Server Error"}), 500

    @app.errorhandler(404)
    def not_found(e):
        return jsonify({"error": "Not Found"}), 404

    @app.errorhandler(500)
    def internal_error(e):
        return jsonify({"error": "Internal Server Error"}), 500

    return app

app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=True)
