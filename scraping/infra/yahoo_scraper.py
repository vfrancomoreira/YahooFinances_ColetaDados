# scraping/infra/yahoo_scraper.py
import requests
from bs4 import BeautifulSoup
from scraping.utils.logger import logger

class YahooScraper:
    @staticmethod
    def fetch_data(ticker):
        url = f"https://finance.yahoo.com/quote/{ticker}"
        headers = {'User-Agent': 'Mozilla/5.0'}
        logger.info(f"Fetching data from {url}")
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Lança uma exceção para status de erro
            logger.info(f"Data fetched successfully from {url}")
            return response.text
        except requests.RequestException as e:
            logger.error(f"Error fetching data from {url}: {e}")
            return None

    @staticmethod
    def parse_html(html):
        if not html:
            logger.warning("HTML is empty or None.")
            return None
        logger.info("Parsing HTML")
        soup = BeautifulSoup(html, 'html.parser')
        return soup
