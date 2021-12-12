# -*- coding: utf-8 -*-

from google.cloud import storage

from .abs_task import ABSTask


class SendToStorageTask(ABSTask):
    """
    Class used to send the buses status saved in a csv file to Google Storage
    """

    def run(self, bucket_name, source_file_name, destination_blob_name):
        """
        Method used to uploads a file to the bucket

        Attributes:
            bucket_name (str): Google Storage's bucket name
            source_file_name (str): Local file path and name
            destination_blob_name (str): Google Storage's object identification
        """

        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)

        blob.upload_from_filename(source_file_name)
