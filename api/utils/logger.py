# logger.py - Simple logger for debugging
import logging
from api.config import config

# Logger configuration
log_file = config["logging"]["log_file"]
verbose = config["logging"]["verbose_console"]

logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log(message):
    """
    Logs message to file and console if verbose is enabled
    """
    logging.info(message)
    if verbose:
        print(message)
