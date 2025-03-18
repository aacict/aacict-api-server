from flask import Blueprint, jsonify,request
from .newsRetrieve import getNews
from .sentimentAnalysis import getSentimentFromText

news_sentiment_bp = Blueprint('news_sentiment', __name__)

@news_sentiment_bp.route('/get-news', methods=['GET'])
def get_news():
    try:
        query = request.args.get('query')
        news = getNews(query)

        return jsonify({"status": "success", "data": news})
    except Exception as e:
        print(e)
        return jsonify({"error": f"An error occurred: {e}"}), 500

@news_sentiment_bp.route('/get-news-sentiment', methods=['POST'])
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