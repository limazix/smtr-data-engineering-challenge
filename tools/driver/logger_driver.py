# -*- coding: utf-8 -*-

import logging
import logging.config


class LoggerDriver:
    """Class designed to access and handle logger operations

    Note:
        This class has to be a singleton
        or it'll create a new logger instance every time it's called

    Atributes:
        _instance (LoggerDriver): reference to itself for singleton purpose
        logger_console (Logger): instance of a logger to write its outputs in
        the console
    """

    _instance = None

    def __init__(self) -> None:
        logging.config.fileConfig("logging.ini")
        self.logger_console = logging.getLogger("console")

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LoggerDriver, cls).__new__(cls)
        return cls._instance
