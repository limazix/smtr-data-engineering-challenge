# -*- coding: utf-8 -*-

from configparser import ConfigParser


class ConfigDriver:
    """This class is designed to easier handle the configuration parameters access

    Attributes:
        configr (ConfigParser): instance for the configuration parser

    """

    def __init__(self):
        self.configr = ConfigParser()
        self.configr.read("config.ini")

    def get_datasource_url(self) -> str:
        """Method used to get the datasource url from the configuration file

        Returns:
            srt: The datasource url

        """
        return self.configr.get("datasource", "DATASOURCE_URL")

    def get_bucket_name(self) -> str:
        """Method used to get the storage bucket name from the configuration file

        Returns:
            str: the storage bucket name
        """
        return self.configr.get("storage", "bucket")
