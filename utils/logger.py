import logging
from logging.handlers import TimedRotatingFileHandler

def setup_logger():
    logger = logging.getLogger("NetworkCheckerBot")
    logger.setLevel(logging.INFO)
    
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    
    file_handler = TimedRotatingFileHandler("bot.log", when="midnight", interval=1, backupCount=7)
    file_handler.setLevel(logging.INFO)
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    return logger
