from api.utils.logger import logger

class DataFormatter:
    @staticmethod
    def format_stock_data(ticker, data):
        if data is None:
            logger.warning(f"Dados vazios para {ticker}.")
            return None

        try:
            price = round(data['Close'].iloc[0], 2)
            change = round(data['Close'].iloc[0] - data['Open'].iloc[0], 2)
            percent_change = round((change / data['Open'].iloc[0]) * 100, 2)

            formatted_change = f"{'+' if change > 0 else ''}{change}"
            formatted_percent_change = f"({'+' if percent_change > 0 else ''}{percent_change}%)"

            formatted_data = {
                'Ticker': ticker,
                'Price': f"{price:.2f}",
                'Change': formatted_change,
                'Percent Change': formatted_percent_change
            }

            logger.info(f"Dados formatados para {ticker}: {formatted_data}")
            return formatted_data

        except Exception as e:
            logger.error(f"Erro ao formatar dados para {ticker}: {e}")
            return None
