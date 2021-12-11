from unittest import TestCase, mock

import requests

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

    def test_run(self):
        """
        it should get all buses status from the datasource and return it
        """
        url = self.task.config.get_datasource_url()
        with mock.patch.object(requests, "get") as mock_get:
            self.task.run()
            mock_get.assert_called_once_with(url)
