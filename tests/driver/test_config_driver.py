from unittest import TestCase, mock

from configparser import ConfigParser

from tools.driver.config_driver import ConfigDriver


class ConfigDriverTest(TestCase):
    def setUp(self) -> None:
        self.driver = ConfigDriver()

    @mock.patch.object(ConfigParser, "read")
    def test_setup(self, mock_read):
        """
        it should setup the config parser using the config.ini file and
        store it in the configr variable
        """
        ConfigDriver()
        self.assertIsInstance(self.driver.configr, ConfigParser)
        mock_read.assert_called_once_with("config.ini")

    def test_get_datasouece_url(self):
        """
        it should return the datasource url as a string
        """
        with mock.patch.object(ConfigParser, "get") as mock_get:
            self.driver.get_datasource_url()
            mock_get.assert_called_once_with("datasource", "DATASOURCE_URL")

        url = self.driver.get_datasource_url()
        self.assertIsInstance(url, str)
