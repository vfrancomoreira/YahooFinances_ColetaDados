import logging
import os

class Logger:
    LOG_DIR = "logs"
    LOG_FILE = "api_fetcher.log"

    @staticmethod
    def setup_logger():
        """Configura o logger para registrar logs em um arquivo e no console."""
        os.makedirs(Logger.LOG_DIR, exist_ok=True)
        log_path = os.path.join(Logger.LOG_DIR, Logger.LOG_FILE)

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            handlers=[
                logging.FileHandler(log_path, encoding="utf-8"),
                logging.StreamHandler()
            ]
        )

        return logging.getLogger("APILogger")

# Criamos uma instância global do logger
logger = Logger.setup_logger()
