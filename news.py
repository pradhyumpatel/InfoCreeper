import requests
from bs4 import BeautifulSoup
import pprint
import pandas as pd
import numpy as np
from newsapi import NewsApiClient

url = 'https://newsapi.org/v2/everything?'

api_key = 'cecd1c1f508a410bbef01f38a4097483'
newsapi = NewsApiClient(api_key)

parameters_10_29 = {
    'q' : 'Wildfire',
    'pageSize' : 100,
    'apiKey' : api_key,
    'language' : 'en',
    'from' : '2020-12-01'
}

response_10_29 = requests.get(url, params = parameters_10_29)
response_json_10_29 = response_10_29.json()

all_articles = newsapi.get_everything(q='tesla',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2021-04-29',
                                      to='2021-03-29',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)
print(all_articles)