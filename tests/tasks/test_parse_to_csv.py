from unittest import TestCase

from tools.tasks.abs_task import ABSTask
from tools.tasks.parse_to_csv_task import ParseToCSVTask


class ParseToCSVTaskTest(TestCase):
    def setUp(self) -> None:
        self.task = ParseToCSVTask()

    def test_setup(self):
        """
        it should be an ABSTask instance
        """
        self.assertIsInstance(self.task, ABSTask)
