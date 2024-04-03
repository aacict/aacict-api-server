from newsRetrieve import getNews
from sentimentAnalysis import getSentimentFromText
from functions import generateCsv

news = getNews()
print("news::::::::::::::::")
print(news)

data = []

for item in news:
    sentiment = getSentimentFromText(item["desc"])
    print("sentiment for the news title: ", item["title"], "::::::::::::::::::::::::::::::::;")
    print(sentiment)
    data.append({**item, **sentiment})

generateCsv(data)

