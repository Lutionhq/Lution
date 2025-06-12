import logging


logging.basicConfig(
    level=logging.INFO,
    format="[LUTION] %(asctime)s %(levelname)s: %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

class log():
    def info(mes) :
        logging.info(mes)
    def warn(mes):
        logging.warning(mes)
    def error(mes):
        logging.error(mes)
    def debug(mes):
        logging.debug(mes)