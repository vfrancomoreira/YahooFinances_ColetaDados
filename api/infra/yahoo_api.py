import yfinance as yf
from api.utils.logger import logger

class YahooFinanceAPI:
    @staticmethod
    def fetch_stock_data(ticker):
        logger.info(f"Buscando dados da API para {ticker}")

        try:
            stock = yf.Ticker(ticker)
            data = stock.history(period="1d")

            if data.empty:
                logger.warning(f"Nenhum dado encontrado para {ticker}.")
                return None

            return data
        except Exception as e:
            logger.error(f"Erro ao acessar API do Yahoo Finance para {ticker}: {e}")
            return None
