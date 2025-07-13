from api.fetch import fetch_news
from api.parse import parse_articles
from storage.save import save_to_csv
from storage.export import export_summary

import logging

if __name__ == "__main__":
    logging.basicConfig(filename="output/news.log", level=logging.INFO)

    API_KEY = "YOUR_API_KEY_HERE"
    articles = fetch_news(API_KEY, 'us', 'business')

    if not articles:
        logging.info("No articles found from fetch_news")
        exit()

    df = parse_articles(articles)

    save_to_csv(df)
    export_summary(df)