from flask import Flask, jsonify, request
from newsRetrieve import getNews
from sentimentAnalysis import getSentimentFromText

app = Flask(__name__)

@app.route('/get-news', methods=['GET'])
def get_news():
    news = getNews()
    return jsonify({"status": "success", "data": news})

@app.route('/get-news-sentiment', methods=['POST'])
def post_data():
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

# Run the Flask server
if __name__ == '__main__':
    app.run(debug=True)
