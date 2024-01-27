import sys

from loguru import logger


def setup_logger(debug: bool) -> None:
    logger.remove()

    if debug:
        logger.add(sys.stdout, level="DEBUG")
    else:
        logger.add(sys.stdout, level="INFO", serialize=True)
