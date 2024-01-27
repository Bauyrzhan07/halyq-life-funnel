import sys
from enum import Enum

from loguru import logger


class StrEnum(str, Enum):
    pass


def setup_logger(debug: bool) -> None:
    logger.remove()

    if debug:
        logger.add(sys.stdout, level="DEBUG")
    else:
        logger.add(sys.stdout, level="INFO", serialize=True)
