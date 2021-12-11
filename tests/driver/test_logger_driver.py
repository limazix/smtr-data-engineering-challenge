from unittest import TestCase, mock

import logging
import logging.config

from tools.driver.logger_driver import LoggerDeriver


class ConfigDriverTest(TestCase):
    @mock.patch.object(logging, "getLogger")
    @mock.patch.object(logging.config, "fileConfig")
    def test_setup(self, mock_fileConfig, mock_getLogger):
        """
        it should setup the logger driver using the logging.ini file
        and instanciate the logger
        """
        LoggerDeriver()
        mock_fileConfig.assert_called_once_with("logging.ini")
        mock_getLogger.assert_called_once_with("console")

    def test_singleton(self):
        """
        it should be a singleton class
        """
        driver1 = LoggerDeriver()
        driver2 = LoggerDeriver()
        self.assertEqual(driver1, driver2)
