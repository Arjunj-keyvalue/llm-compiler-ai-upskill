import logging
from .config import settings

def get_logger(name: str):
    log_level = getattr(logging, settings.log_level.upper(), logging.INFO)
    logging.basicConfig(level=log_level)
    logger = logging.getLogger(name)
    return logger