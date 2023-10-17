import os
from datetime import datetime, timedelta, timezone


class StorageUtils:

    def has_extension(self, filename):
        extension = os.path.splitext(filename)[-1]
        return extension != "" and "." in extension

    def get_extension(self, filename):
        if not self.has_extension(filename):
            raise ValueError("File does not have an extension.")
        return os.path.splitext(filename)[-1]

    def is_json(self, filename):
        return self.get_extension(filename) == ".json"

    def generate_blob_path(self, *args) -> str:
        """Generates a blob path for a file.

        Args:
            path: The path to the file.
            filename: The name of the file.

        Returns:
            The file path in the format '{path}/{filename}'.
        """

        if any(
            char in arg for arg in args for char in [":", "*", "?", '"', "<", ">", "|"]
        ):
            raise ValueError("Invalid character in path.")

        return self.join_directories(*args)

    def created_over_one_month_ago(self, date_created: datetime) -> bool:
        """Checks if a datetime is over one month old.

        Args:
            date_created: The datetime to check.

        Returns:
            True if the datetime is over one month old, False otherwise.
        """
        if date_created.tzinfo is not None:
            current_time = datetime.now(timezone.utc)
        else:
            current_time = datetime.now()

        return date_created < current_time - timedelta(days=30)

    def join_directories(self, *args):
        if any(arg for arg in args if self.has_extension(arg)):
            return os.path.join(*args).replace("\\", "/")
        return os.path.join(*args).replace("\\", "/") + "/"


storage_utils = StorageUtils()
