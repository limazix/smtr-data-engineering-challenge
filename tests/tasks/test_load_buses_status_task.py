from unittest import TestCase, mock

import requests
from requests.models import HTTPError

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

    def test_failed_request(self):
        """
        it should rise an exception if the requests falis and log its error
        """
        with mock.patch.object(requests, "get") as mock_get, mock.patch.object(
            self.task.logger, "error"
        ) as mock_logger_error:
            mock_get.side_effect = requests.exceptions.HTTPError()

            self.task.run()
            self.assertRaises(HTTPError)
            mock_logger_error.assert_called_once()
