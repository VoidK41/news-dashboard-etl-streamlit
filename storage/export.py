import pandas as pd
import logging

def export_summary(df, output='output/news_summary.csv'):
    logging.info("Creating summary 'total_articles' by 'source' ")

    try:
        summary = df.groupby('source')['title'].count().reset_index()
        summary.columns = ['source', 'total_articles']
        summary.to_csv(output, index=False)
        logging.info("news_summary saved to %s with shape %s",output, summary.shape)

    except Exception as e:
        logging.error("Failed to export data to csv: %s",e)