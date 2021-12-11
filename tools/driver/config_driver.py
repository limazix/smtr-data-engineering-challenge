# -*- coding: utf-8 -*-

from configparser import ConfigParser

class ConfigDriver:
    """ConfigDriver

    This class is designed to easier handle the configuration parameters access

    Attributes:
        configr (ConfigParser): instance for the configuration parser
        
    """

    def __init__(self):
        self.configr = ConfigParser()
        self.configr.read('config.ini')
