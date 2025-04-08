# scraping/application/data_formatter.py
from scraping.utils.logger import logger

class DataFormatter:
    @staticmethod
    def extract_stock_data(soup, ticker):
        logger.info(f"Iniciando extract_stock_data para {ticker}")
        data = {
            'Ticker': ticker,
            'Price': None,
            'Change': None,
            'Percent Change': None
        }

        if not soup:
            logger.warning(f"Não foi possível analisar os dados para {ticker}.")
            return data

        try:
            price_element = soup.find('span', class_='price yf-15b2o7n')
            data['Price'] = DataFormatter._extract_price(price_element)

            change_element_positive = soup.find('span', class_='base txt-positive yf-ipw1h0')
            change_element_negative = soup.find('span', class_='base txt-negative yf-ipw1h0')
            data['Change'] = DataFormatter._extract_value(change_element_positive, change_element_negative)

            percent_change_span_positive = soup.find('span', class_='positive yf-15b2o7n')
            percent_change_span_negative = soup.find('span', class_='negative yf-15b2o7n')
            data['Percent Change'] = DataFormatter._extract_value(percent_change_span_positive, percent_change_span_negative)

        except AttributeError as e:
            logger.error(f"Erro ao extrair dados para {ticker}: {e}")
        except ValueError as ve:
            logger.error(f"Erro ao converter valores para {ticker}: {ve}")

        return data

    @staticmethod
    def _extract_price(price_element):
        if price_element:
            try:
                return float(price_element.text.replace(',', ''))
            except ValueError:
                logger.error(f"Could not convert price to float: {price_element.text}")
                return None
        return None

    @staticmethod
    def _extract_value(element_positive, element_negative):
        if element_positive:
            value = element_positive.text.strip()
            logger.debug(f"Valor extraido: {value}")
            return value
        elif element_negative:
            value = element_negative.text.strip()
            logger.debug(f"Valor extraido: {value}")
            return value
        return None
