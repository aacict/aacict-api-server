from flask import Flask, jsonify
from flask_cors import CORS
from projects.news_sentiment_analysis.routes import news_sentiment_bp
from projects.object_detection.routes import object_detection_bp
from config import config
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'projects')))

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["https://thapaashish.com.np", "http://localhost:5173", config.APP_URL]}})

app.register_blueprint(news_sentiment_bp, url_prefix='/news_sentiment')
app.register_blueprint(object_detection_bp, url_prefix='/object_detection')

@app.route('/', methods=['GET'])
def home():
    try:
        return jsonify({"status": "success", "data": "Test Home Route"})
    except Exception as e:
        print(e)
        return jsonify({"error": f"An error occurred: {e}"}), 500

# Run the Flask server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7860)
