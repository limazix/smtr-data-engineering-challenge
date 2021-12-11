from unittest import TestCase

import json

from tools.tasks.abs_task import ABSTask
from tools.tasks.parse_to_csv_task import ParseToCSVTask


class ParseToCSVTaskTest(TestCase):
    def setUp(self) -> None:
        self.task = ParseToCSVTask()

        with open("tests/tasks/mock_data.json") as d:
            self.data = json.load(d)

    def test_setup(self):
        """
        it should be an ABSTask instance
        """
        self.assertIsInstance(self.task, ABSTask)

    def test_build_header(self):
        """
        it should return all bus status attributes as
        a string separated by comma
        """
        status = self.data[0]
        keys = sorted(status.keys())
        expected_header = ",".join(keys)

        header = self.task.build_header(status)
        self.assertEqual(expected_header, header)
