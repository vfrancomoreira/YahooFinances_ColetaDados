import requests
from bs4 import BeautifulSoup
from scraping.utils.logger import logger

class YahooScraper:
    BASE_URL = 'https://finance.yahoo.com/quote/'

    @staticmethod
    def fetch_data(ticker):
        url = f'{YahooScraper.BASE_URL}{ticker}'
        headers = {'User-Agent': 'Mozilla/5.0'}

        logger.info(f"Coletando dados para {ticker} em {url}")

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            logger.error(f"Erro ao acessar {url}: {e}")
            return None

    @staticmethod
    def parse_html(html):
        return BeautifulSoup(html, 'html.parser') if html else None
