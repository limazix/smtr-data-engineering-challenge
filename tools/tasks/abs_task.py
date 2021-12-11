# -*- coding: utf-8 -*-

from prefect.core.task import Task

from ..driver.config_driver import ConfigDriver


class ABSTask(Task):
    """Class designed to hold the basic structura for a task

    Note:
        It will follow the Template Method design pattern

    Attributes:
        config (ConfigDriver): instance for the project configuration
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config = ConfigDriver()
