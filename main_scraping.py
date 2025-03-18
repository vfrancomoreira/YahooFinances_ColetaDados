from scraping.infra.yahoo_scraper import YahooScraper
from scraping.application.data_formatter import DataFormatter
from scraping.persistence.csv_exporter import CSVExporter
from scraping.utils.logger import logger

def main():
    ticker = 'AAPL'  # Exemplo: Apple Inc.

    logger.info(f"Iniciando scraping para {ticker}")

    try:
        html = YahooScraper.fetch_data(ticker)
        soup = YahooScraper.parse_html(html)
        data = DataFormatter.extract_stock_data(soup, ticker)

        if data['Price'] is not None:
            CSVExporter.save_to_csv(data)
        else:
            logger.warning("Não foi possível extrair os dados.")

    except Exception as e:
        logger.critical(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()
