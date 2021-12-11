from configparser import ConfigParser
from unittest import TestCase

from tools.driver.config_driver import ConfigDriver


class ConfigDriverTest(TestCase):
    def setUp(self) -> None:
        self.driver = ConfigDriver()

    def test_setup(self):
        """
        it should setup the config parser using the config.ini file and
        store it in the configr variable
        """
        file = open("config.ini", "r")
        file_contents = [line.replace("\n", "") for line in file.readlines()]
        for section in self.driver.configr.sections():
            self.assertIn("[{}]".format(section), file_contents)
        self.assertIsInstance(self.driver.configr, ConfigParser)
