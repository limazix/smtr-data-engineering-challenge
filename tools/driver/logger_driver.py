# -*- coding: utf-8 -*-

import logging
import logging.config


class LoggerDeriver:
    """Class designed to access and handle logger operations

    Atributes:
        logger_console (Logger): instance of a logger to write its outputs in
        the console
    """

    def __init__(self) -> None:
        logging.config.fileConfig("logging.ini")
        self.logger_console = logging.getLogger("console")
