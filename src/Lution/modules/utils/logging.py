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
    @staticmethod
    def info(mes, logger="LUTION") :
        logging.basicConfig(format=f"{logger} %(asctime)s %(levelname)s: %(message)s")
        logging.info(mes)
    @staticmethod
    def warn(mes, logger="LUTON"):
        logging.basicConfig(format=f"{logger} %(asctime)s %(levelname)s: %(message)s")
        logging.warning(mes)
    @staticmethod
    def error(mes, logger="LUTION"):
        logging.basicConfig(format=f"{logger} %(asctime)s %(levelname)s: %(message)s")
        logging.error(mes)
    @staticmethod
    def debug(mes, logger="LUTION"):
        logging.basicConfig(format=f"{logger} %(asctime)s %(levelname)s: %(message)s")
        logging.debug(mes)
