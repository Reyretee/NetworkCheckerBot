from config.config import Config
from handlers.ping_handler import PingHandler
from server import start_server
from utils.logger import setup_logger


def main():
    logger = setup_logger()
    logger.info("NetworkCheckerBot başlatılıyor.")

    ping_handler = PingHandler(logger)
    

    try:
        start_server(Config.SERVER_HOST, Config.SERVER_PORT, ping_handler, logger)
    except KeyboardInterrupt:
        logger.info("Bot durduruluyor.")
    except Exception as e:
        logger.error(f"Bir hata oluştu: {e}")

if __name__ == "__main__":
    main()