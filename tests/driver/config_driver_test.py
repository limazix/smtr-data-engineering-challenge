from unittest import TestCase

from tools.driver.config_driver import ConfigDriver


class ConfigDriverTest(TestCase):
    def setUp(self) -> None:
        self.driver = ConfigDriver()

    def test_setup(self):
        self.assertListEqual(self.driver.configr.sections(), ["datasource"])
