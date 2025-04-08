# main.py
from scraping.infra.yahoo_scraper import YahooScraper
from scraping.application.data_formatter import DataFormatter
from scraping.persistence.csv_exporter import CSVExporter
from scraping.utils.logger import logger

def main():
    ticker = 'AAPL'

    logger.info(f"Iniciando scraping para {ticker}")

    try:
        html = YahooScraper.fetch_data(ticker)
        if html is None:
            logger.error("Failed to fetch HTML. Exiting.")
            return

        soup = YahooScraper.parse_html(html)
        if soup is None:
            logger.error("Failed to parse HTML. Exiting.")
            return

        data = DataFormatter.extract_stock_data(soup, ticker)

        if data['Price'] is not None:
            CSVExporter.save_to_csv(data)
        else:
            logger.warning("Não foi possível extrair os dados.")

    except Exception as e:
        logger.critical(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()
