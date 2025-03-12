from flask import Flask, jsonify, request
from newsRetrieve import getNews

app = Flask(__name__)

@app.route('/get-news', methods=['GET'])
def get_news():
    news = getNews()
    return jsonify({"status": "success", "data": news})

@app.route('/get-news-sentiment', methods=['POST'])
def post_data():
    data = request.get_json()  # Get JSON data from request
    news = data.get("news")

    for item in news:
        description = item["desc"] or item["title"]
        sentiment = getSentimentFromText(description)
        print("sentiment for the news title: ", item["title"], "::::::::::::::::::::::::::::::::;")
        print(sentiment)
        data.append({**item, **sentiment})

    if len(news) == 0 or news is None:
        return jsonify({"error": "No data provided"}), 400

    return jsonify({"message": "Data received successfully!", "data": news})

# Run the Flask server
if __name__ == '__main__':
    app.run(debug=True)
