from unittest import TestCase

from tools.driver.config_driver import ConfigDriver
from tools.tasks.abs_task import ABSTask


class ABSTaskTest(TestCase):
    def setUp(self) -> None:
        self.task = ABSTask()

    def test_setup(self):
        """
        it should have a config instance as an attribute
        """
        self.assertIsInstance(self.task.config, ConfigDriver)
