from unittest import TestCase

from logging import Logger

from tools.tasks.abs_task import ABSTask


class ABSTaskTest(TestCase):
    def setUp(self) -> None:
        self.task = ABSTask()

    def test_setup(self):
        """
        it should have a logger instance as an attribute
        """
        self.assertIsInstance(self.task.logger, Logger)
