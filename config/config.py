from dotenv import load_dotenv
load_dotenv() 
import os
NEWS_DATA_API_KEY = os.environ.get('NEWS_DATA_API_KEY')
APP_URL = os.environ.get('APP_URL')