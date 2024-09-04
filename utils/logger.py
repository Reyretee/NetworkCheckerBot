import logging
from config.config import Config

def setup_logger():
    logger = logging.getLogger("NetworkCheckerBot")
    logger.setLevel(getattr(logging, Config.LOG_LEVEL.upper(), logging.INFO))


    file_handler = logging.FileHandler(Config.LOG_FILE)
    file_handler.setLevel(getattr(logging, Config.LOG_LEVEL.upper(), logging.INFO))


    console = logging.StreamHandler()
    console.setLevel(getattr(logging, Config.LOG_LEVEL.upper(), logging.INFO))


    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console.setFormatter(formatter)


    logger.addHandler(file_handler)
    logger.addHandler(console)


    return logger