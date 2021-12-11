from unittest import TestCase

from tools.tasks.abs_task import ABSTask
from tools.tasks.load_buses_status_task import LoadBusesStatusTask


class LoadBusesStatusTaskTest(TestCase):
    def setUp(self) -> None:
        self.task = LoadBusesStatusTask()

    def test_setup(self):
        """
        it should be an ABSTask instance
        """
        self.assertIsInstance(self.task, ABSTask)
