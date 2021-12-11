# -*- coding: utf-8 -*-

import logging
import logging.config


class LoggerDeriver:
    """Class designed to access and handle logger operations"""

    def __init__(self) -> None:
        logging.config.fileConfig("logging.ini")
