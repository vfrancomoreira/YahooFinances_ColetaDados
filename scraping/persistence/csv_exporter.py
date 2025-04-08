# scraping/persistence/csv_exporter.py
import csv
import os
from datetime import datetime
from scraping.utils.logger import logger

class CSVExporter:
    @staticmethod
    def save_to_csv(data):
        file_path = 'data/dados_yahoo_scraping.csv'
        fieldnames = ['Ticker', 'Price', 'Change', 'Percent Change', 'Date']

        # Adiciona a data atual ao dicionário de dados
        data['Date'] = datetime.now().strftime('%Y-%m-%d')

        file_exists = os.path.exists(file_path)

        try:
            with open(file_path, 'a', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                if not file_exists:
                    writer.writeheader()

                writer.writerow(data)
                logger.info(f"Dados salvos com sucesso em {file_path}")

        except Exception as e:
            logger.error(f"Erro ao salvar dados em {file_path}: {e}")
