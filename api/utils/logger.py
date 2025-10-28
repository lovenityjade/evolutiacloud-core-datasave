import logging
from api.config import config

log_file = config["logging"]["log_file"]
verbose = config["logging"]["verbose_console"]

logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log(message):
    logging.info(message)
    if verbose:
        print(message)
