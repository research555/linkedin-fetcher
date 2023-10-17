from app.core import settings
from app.utils import storage_utils
import time
from google.cloud import storage
from google.oauth2 import service_account
import json
from typing import Any, Dict
from pathlib import Path


class GoogleCloudStorage:
    def __init__(self):

        credentials = service_account.Credentials.from_service_account_file(
            settings.GCP_SERVICE_ACCOUNT_KEY_POINTER
        )

        storage_client = storage.Client(credentials=credentials)
        bucket_name = settings.LINKEDIN_BUCKET_NAME
        self.bucket = storage_client.bucket(bucket_name)
        self.bucket_relative_file_path = settings.LINKEDIN_BUCKET_RELATIVE_FILE_PATH

    def __upload_blob(self, blob_path: str, source_json: str) -> str:
        if not storage_utils.has_extension(blob_path):
            raise ValueError("Invalid file path. No extension found.")
        if not storage_utils.is_json(blob_path):
            raise ValueError(
                "Invalid content type. Only '.json' is supported currently."
            )

        blob = self.bucket.blob(blob_path)
        blob.upload_from_string(source_json, content_type="application/json")

        return storage_utils.join_directories(blob_path)

    def upload_blob(self, base_folder: str, subfolder: str, filename: str, data: str, extension: str = ".json") -> str:
        """Uploads a file to the bucket if it doesn't exist or if it's over a month old."""

        if not storage_utils.has_extension(filename):
            filename = filename + extension
        blob_path = storage_utils.generate_blob_path(self.bucket_relative_file_path, base_folder, subfolder, filename)
        if self.path_exists(blob_path):  # If blob exists
            created_time = self.get_blob_time_created(blob_path)
            if not storage_utils.created_over_one_month_ago(created_time):
                print("Upload aborted: Blob is not over a month old.")
                return blob_path
            print("Uploading blob: Blob is over a month old.")

        retry_count = 0
        while retry_count < 3:
            try:
                return self.__upload_blob(blob_path=blob_path, source_json=data)
            except Exception as e:
                retry_count += 1
                time.sleep(2)
                if retry_count == 3:
                    raise e

    def retrieve_blob_data(self, base_folder: str, subfolder: str, filename: str, extension: str = ".json") -> Any:
        """Retrieve the data from a blob if it exists, else return None."""

        if not storage_utils.has_extension(filename):
            filename = filename + extension
        blob_path = storage_utils.generate_blob_path(self.bucket_relative_file_path, base_folder, subfolder, filename)
        if not self.path_exists(blob_path):
            return None

        created_time = self.get_blob_time_created(blob_path)
        if storage_utils.created_over_one_month_ago(self.get_blob_time_created(blob_path)):
            print("Overwriting blob: Blob is over a month old and needs to be updated.")
            return None

        print("Downloading blob: Blob is not over a month old.")
        return self.download_blob_to_json(blob_path)

    def download_blob_to_json(self, blob_path: str) -> Any:
        """Downloads a JSON file from the bucket."""

        if blob_path.endswith("/"):
            blobs = list(self.bucket.list_blobs(prefix=blob_path))
            if len(blobs) == 1:
                return json.loads(blobs[0].download_as_string())
            else:
                data = []
                for blob in blobs:
                    data.append(json.loads(blob.download_as_string()))
                return data
        else:
            blob = self.bucket.blob(blob_path)
            if blob.exists():
                return json.loads(blob.download_as_string())
            else:
                return None

    def path_exists(self, path: str):
        """Checks if a directory exists in the bucket."""
        if storage_utils.has_extension(path):
            blob = self.bucket.blob(path)
            return blob.exists()
        blobs = self.bucket.list_blobs(prefix=path)
        return any(blobs)

    def get_blob(self, blob_path: str):
        """Gets a blob from the bucket."""
        blob = self.bucket.blob(blob_path)
        return blob


    def get_blob_time_created(self, blob_path: str) -> Dict[str, Any]:
        """Get created datetime for a blob in the bucket."""
        blob = self.bucket.blob(blob_path)
        blob.reload()
        if blob.exists():
            return blob.time_created
        else:
            return {}
    def get_blob_time_updated(self, blob_path: str) -> Dict[str, Any]:
        """Get updated datetime for a blob in the bucket."""
        blob = self.bucket.blob(blob_path)
        if blob.exists():
            return blob.updated
        else:
            return {}

gcs = GoogleCloudStorage()