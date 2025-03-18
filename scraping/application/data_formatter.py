from scraping.utils.logger import logger

class DataFormatter:
    @staticmethod
    def extract_stock_data(soup, ticker):
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
            # Preço
            price_element = soup.find('fin-streamer', {'data-field': 'regularMarketPrice'})
            data['Price'] = float(price_element.text.replace(',', '')) if price_element else None

            # Mudança
            change_element = soup.find('fin-streamer', {'data-field': 'regularMarketChange'})
            change = float(change_element.text.replace(',', '')) if change_element else None

            # Porcentagem de mudança
            percent_change_element = soup.find('fin-streamer', {'data-field': 'regularMarketChangePercent'})
            percent_change_str = percent_change_element.text.strip() if percent_change_element else None
            percent_change_value = percent_change_str.replace('(', '').replace(')', '').replace('%', '').strip() if percent_change_str else None
            percent_change = float(percent_change_value) if percent_change_value else None

            # Formatar os dados
            data['Change'] = f"{'+' if change > 0 else ''}{change:.2f}" if change is not None else None
            data['Percent Change'] = f"({'+' if percent_change > 0 else ''}{percent_change:.2f}%)" if percent_change is not None else None
            data['Price'] = f"{data['Price']:.2f}" if data['Price'] is not None else None

            logger.info(f"Dados extraídos com sucesso para {ticker}: {data}")

        except AttributeError as e:
            logger.error(f"Erro ao extrair dados para {ticker}: {e}")
        except ValueError as ve:
            logger.error(f"Erro ao converter valores para {ticker}: {ve}")

        return data
