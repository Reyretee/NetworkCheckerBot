import asyncio
from config.config import Config
from utils.logger import setup_logger
from handlers.ping_handler import PingHandler
from server import start_async_server

def main():
    logger = setup_logger()
    logger.info("NetworkCheckerBot başlatılıyor...")
    
    ping_handler = PingHandler(logger)

    try:
        asyncio.run(start_async_server(Config.SERVER_HOST, Config.SERVER_PORT, ping_handler, logger))
    except KeyboardInterrupt:
        logger.info("NetworkCheckerBot durduruluyor...")
    except Exception as e:
        logger.error(f"Async sunucu başlatılırken bir hata oluştu: {e}")

if __name__ == "__main__":
    main()
