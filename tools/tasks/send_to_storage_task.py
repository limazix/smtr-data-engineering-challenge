# -*- coding: utf-8 -*-

import os
from google.cloud import storage

from .abs_task import ABSTask


class SendToStorageTask(ABSTask):
    """
    Class used to send the buses status saved in a csv file to Google Storage
    """

    def run(self, file_name):
        """
        Method used to uploads a file to the bucket

        Attributes:
            file_name (str): Local file path and name
        """

        bucket_name = self.config.get_bucket_name()

        try:
            storage_client = storage.Client()
            bucket = storage_client.bucket(bucket_name)
            blob = bucket.blob(file_name)

            blob.upload_from_filename(file_name)

            os.remove(file_name)
        except Exception as err:
            self.logger.error(err)
