from api.infra.yahoo_api import YahooFinanceAPI
from api.application.data_formatter import DataFormatter
from api.persistence.csv_exporter import CSVExporter
from api.utils.logger import logger

def main():
    ticker = 'AAPL'  # Exemplo: Apple Inc.

    logger.info(f"Iniciando coleta de dados via API para {ticker}")

    try:
        raw_data = YahooFinanceAPI.fetch_stock_data(ticker)
        formatted_data = DataFormatter.format_stock_data(ticker, raw_data)

        if formatted_data:
            CSVExporter.save_to_csv(formatted_data)
        else:
            logger.warning(f"Não foi possível salvar os dados para {ticker}")

    except Exception as e:
        logger.critical(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()
