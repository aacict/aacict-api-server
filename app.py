from flask import Flask, jsonify, request
from newsRetrieve import getNews
from sentimentAnalysis import getSentimentFromText
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv() 
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["https://thapaashish.com.np", "http://localhost:5173", os.getenv("APP_URL")]}})

@app.route('/', methods=['GET'])
def home():
    try:
        return jsonify({"status": "success", "data": "Test Home Route"})
    except Exception as e:
        print(e)
        return jsonify({"error": f"An error occurred: {e}"}), 500

@app.route('/get-news', methods=['GET'])
def get_news():
    try:
        query = request.args.get('query')
        news = getNews(query)

        return jsonify({"status": "success", "data": news})
    except Exception as e:
        print(e)
        return jsonify({"error": f"An error occurred: {e}"}), 500

@app.route('/get-news-sentiment', methods=['POST'])
def post_data():
    try:
        data = request.get_json()
        news = data.get("news")


        if len(news) == 0 or news is None:
            return jsonify({"error": "No data provided"}), 400
        
        res=[]
        for item in news:
            print("item: ", item)
            description = item["desc"] or item["title"]

            try:
                sentiment = getSentimentFromText(description)
                print("sentiment for the news title: ", item["title"], "::::::::::::::::::::::::::::::::;")
                print(sentiment)
            except Exception as e:
                print(f"Error occurred while getting sentiment for {item['title']}: {e}")
                sentiment = {}  # Assigning an empty dictionary in case of error

            res.append({**item, **sentiment})
            
        return jsonify({"message": "Data received successfully!", "data": res})
    except Exception as e:
        print(e)
        return jsonify({"error": f"An error occurred: {e}"}), 500

# Run the Flask server
if __name__ == '__main__':
    app.run(debug=True)
