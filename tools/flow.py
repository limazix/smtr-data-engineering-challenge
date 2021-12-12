# -*- coding: utf-8 -*-

from prefect import Flow
from prefect.core import Edge

from .tasks.load_buses_status_task import LoadBusesStatusTask
from .tasks.parse_to_csv_task import ParseToCSVTask
from .tasks.send_to_storage_task import SendToStorageTask


load_buses_status_task = LoadBusesStatusTask()
parse_to_csv_task = ParseToCSVTask()
send_to_storage_task = SendToStorageTask()

load_edge = Edge(load_buses_status_task, parse_to_csv_task, key="data")


Flow(
    name="StoreBusesStatus",
    edges=[load_edge],
    tasks=[load_buses_status_task, parse_to_csv_task],
).run()
