from newsdataapi import NewsDataApiClient
from config import config

api = NewsDataApiClient(apikey=config.NEWS_DATA_API_KEY)

def getNews(query='ronaldo', country= 'us', language='en'):
  response = api.news_api( q = query, country = country, language = language)
  data = []
  for res in response['results']:
    data.append({"title":res['title'], "desc":res['description'] })
  return data