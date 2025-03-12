from newsdataapi import NewsDataApiClient
from dotenv import load_dotenv
import os

load_dotenv() 

api = NewsDataApiClient(apikey=os.getenv("NEWDATA_API_KEY"))

def getNews(query='ronaldo', country= 'us', language='en'):
  response = api.news_api( q = query, country = country, language = language)
  data = []
  for res in response['results']:
    data.append({"title":res['title'], "desc":res['description'] })
  return data