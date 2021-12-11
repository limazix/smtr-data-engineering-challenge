# -*- coding: utf-8 -*-

import requests

from .abs_task import ABSTask


class LoadBusesStatusTask(ABSTask):
    """
    Class used to load the latest buses status

    """

    def run(self):
        """
        Method used to load the latest buses status from the datasource

        Returns:
            list: All buses status
        """
        response = requests.get(self.config.get_datasource_url())
        return response.json()
