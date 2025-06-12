import logging


logging.basicConfig(
    level=logging.INFO,
    format="[LUTION] %(asctime)s %(levelname)s: %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)