from unittest import TestCase

import json
from unittest.case import skip

from tools.tasks.abs_task import ABSTask
from tools.tasks.parse_to_csv_task import ParseToCSVTask


class ParseToCSVTaskTest(TestCase):
    def setUp(self) -> None:
        self.task = ParseToCSVTask()

        with open("tests/tasks/mock_data.json") as d:
            self.data_json = json.load(d)

        with open("tests/tasks/mock_data.csv") as d:
            self.data_csv = d.readlines()

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
        status = self.data_json[0]
        keys = status.keys()
        expected_header = ",".join(keys)

        header = self.task.build_header(status)
        self.assertEqual(expected_header, header)

    @skip
    def test_build_body(self):
        """
        it should return the csv body with all buses stus data
        """
        status = self.data_json[0]
        headers = sorted(status.keys())
        expected_body = self.data_csv[1:]

        body = self.task.build_body(self.data_json, headers)
        self.assertEqual(expected_body, body)
