from newsdataapi import NewsDataApiClient

api = NewsDataApiClient(apikey="your_api_key")

def getNews():
  response = api.news_api( q= "ronaldo" , country = "us")
  data = []
  for res in response['results']:
    data.append({"title":res['title'], "desc":res['description'] })
  return data