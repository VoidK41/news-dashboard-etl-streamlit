import pandas as pd
import logging

def parse_articles(articles):
    logging.info("Parsing %d articles",len(articles))

    records = []
    for article in articles:
        record = {
            'title' : article.get('title'),
            'source' : article.get('source', {}).get('name'),
            'url' : article.get('url'),
            'published_at' : article.get('publishedAt')
        }
        records.append(record)

    df = pd.DataFrame(records)
    logging.info("Success parsing articles with shape: %s",df.shape)
    return df