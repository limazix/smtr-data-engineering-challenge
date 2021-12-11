from configparser import ConfigParser
from unittest import TestCase

from tools.driver.config_driver import ConfigDriver


class ConfigDriverTest(TestCase):
    def load_config_file(self) -> None:
        file = open("config.ini", "r")
        self.config = [line.replace("\n", "") for line in file.readlines()]
        file.close()

    def setUp(self) -> None:
        self.driver = ConfigDriver()
        self.load_config_file()

    def test_setup(self):
        """
        it should setup the config parser using the config.ini file and
        store it in the configr variable
        """
        for section in self.driver.configr.sections():
            self.assertIn("[{}]".format(section), self.config)
        self.assertIsInstance(self.driver.configr, ConfigParser)

    def test_get_datasouece_url(self):
        """
        it should return the datasource url as a string
        """
        url = self.config[1].split("=")[1]
        self.assertEqual(url, self.driver.get_datasource_url())
