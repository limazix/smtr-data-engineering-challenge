# -*- coding: utf-8 -*-

from prefect.core.task import Task

from ..driver.logger_driver import LoggerDriver


class ABSTask(Task):
    """Class designed to hold the basic structura for a task

    Note:
        It will follow the Template Method design pattern

    Attributes:
        logger (Logger): instance for the logger
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        logger_driver = LoggerDriver()
        self.logger = logger_driver.logger_console
