from unittest import TestCase

from tools.tasks.abs_task import ABSTask
from tools.tasks.send_to_storage_task import SendToStorageTask


class SendToStorageTaskTest(TestCase):
    def setUp(self) -> None:
        self.task = SendToStorageTask()

    def test_setup(self):
        """
        it should be an ABSTask instance
        """
        self.assertIsInstance(self.task, ABSTask)
