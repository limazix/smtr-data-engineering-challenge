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
        headers = data.keys()
        return ",".join(headers) + "\n", headers

    def build_body(self, data: list, headers: list):
        """
        Method used to build the csv body with the buses status data

        Attributes:
            data (list): all buses status
            headers (list): sorted csv headers

        Returns:
            str: a string with all buses status contents
        """
        body = ""

        for status in data:
            row = []
            for header in headers:
                row.append(str(status[header]))
            body += ",".join(row) + "\n"

        return body

    def write_csv(self, csv: str):
        """
        Method used to create a csv file with all buses status

        Attributes:
            csv (srt): buses status data organized as csv structure
        """
        with open("data.csv", "w+") as f:
            f.write(csv)

    def run(self, data: list):
        """
        Method used to control the transformation process

        Attributes:
            data (list): list of all buses status
        """
        header, headers = self.build_header(data)
        body = self.build_body(data, headers)
        csv = header + body
        self.write_csv(csv)
