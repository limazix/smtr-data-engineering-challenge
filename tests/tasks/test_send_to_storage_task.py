from unittest import TestCase, mock

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

    def test_file_existence(self):
        """
        it should rise an exception if the file path not exists
        """
        with mock.patch.object(self.task.logger, "error") as mock_logger_error:
            self.task.run("some-bucket", "missing.csv", "blob-destination")
            self.assertRaises(FileNotFoundError)
            mock_logger_error.assert_called_once()
