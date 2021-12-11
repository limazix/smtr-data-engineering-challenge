# -*- coding: utf-8 -*-

from .abs_task import ABSTask


class ParseToCSVTask(ABSTask):
    """
    Class designed to transform the JSON data into a CSV file
    """

    def build_header(self, data: dict):
        """
        Method used to build the csv header

        Attributes:
            data (dict): dictionary with a single bus status

        Returns:
            str: a string with all column names separated by comma
        """
        headers = sorted(data.keys())
        return ",".join(headers)

    def run(self, data: list):
        """
        Method used to control the transformation process

        Attributes:
            data (list): list of all buses status
        """
        pass
