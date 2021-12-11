from unittest import TestCase, mock

import logging
import logging.config

from tools.driver.logger_driver import LoggerDeriver


class ConfigDriverTest(TestCase):
    def setUp(self) -> None:
        self.driver = LoggerDeriver()

    @mock.patch.object(logging.config, "fileConfig")
    def test_setup(self, mock_fileConfig):
        """
        it should setup the logger driver using the logging.ini file
        """
        LoggerDeriver()
        mock_fileConfig.assert_called_once_with("logging.ini")
