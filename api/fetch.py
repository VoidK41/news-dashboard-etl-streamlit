import requests
import logging

def fetch_news(api_key, country='us', category=None):
    logging.info("Fetching top headline from News API")

    url = "https://newsapi.org/v2/top-headlines"
    params = {
        'country':country,
        'apiKey':api_key
    }

    if category:
        params['category'] = category

    response = requests.get(url, params=params)
    if response.status_code == 200 :
        logging.info("Success fetching data from API")
        return response.json()['articles']
    else:
        logging.error("Failed to fetch data. Status Code: %s ", response.status_code)
        return []