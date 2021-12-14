# -*- coding: utf-8 -*-

import time
import requests
import prefect
from prefect.engine.signals import LOOP

from .abs_task import ABSTask


class LoadBusesStatusTask(ABSTask):
    """
    Class used to load the latest buses status
    """

    def run(self):
        """Method used to load the latest buses status from the datasource

        Returns:
            list: All buses status
        """

        loop_payload = prefect.context.get("task_loop_result", {})
        i = loop_payload.get("i", 0)
        stat = loop_payload.get("stat", [])

        try:
            response = requests.get(self.config.get_datasource_url())
            response.raise_for_status()
            stat.extend(response.json())
        except Exception as err:
            self.logger.error(err.strerror)

        if i == 9:
            return stat

        time.sleep(60)

        raise LOOP(message="#{}".format(i), result=dict(i=i + 1, stat=stat))
