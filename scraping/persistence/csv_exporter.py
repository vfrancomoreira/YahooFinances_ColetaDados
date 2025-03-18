import pandas as pd
import os
from datetime import datetime
from scraping.utils.logger import logger

class CSVExporter:
    @staticmethod
    def save_to_csv(data, filename='dados_yahoo_scraping.csv'):
        os.makedirs('data', exist_ok=True)
        filepath = os.path.join('data', filename)

        # Adicionar a data atual ao objeto coletado
        data['Date'] = datetime.now().strftime("%Y-%m-%d")

        try:
            # Verifica se o arquivo já existe
            if os.path.exists(filepath):
                df = pd.read_csv(filepath)
                df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)  # Adiciona nova linha
            else:
                df = pd.DataFrame([data])  # Cria novo CSV

            df.to_csv(filepath, index=False)  # Salva sem sobrescrever os dados anteriores
            logger.info(f"Dados salvos com sucesso em {filepath}")

        except Exception as e:
            logger.error(f"Erro ao salvar CSV: {e}")
