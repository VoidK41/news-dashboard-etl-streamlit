import logging

def save_to_csv(df, output_path='output/news.csv'):
    logging.info("Trying to save DataFrame to csv at: %s",output_path)

    try:
        df.to_csv(output_path, index=False)
        logging.info("Success save 'news.csv' with shape %s to %s",df.shape,output_path)

    except Exception as e:
        logging.error("Failed to saved CSV: %s",str(e))