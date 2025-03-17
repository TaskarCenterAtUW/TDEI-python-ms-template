# Class for Storage service.

from python_ms_core import Core
from src.config import Settings

class StorageService:
    """
    Class for handling storage operations.
    Use this class for uploading and downloading files to and from a remote storage location.
    """

    def __init__(self, core: Core) -> None:
        self.storage_client = core.get_storage_client()
        # TODO : Change storage location
        self.config = Settings()
        self.storage_container = self.storage_client.get_container(self.config.storage_container_name)

    def upload_local_file(self, local_path: str, remote_path: str) -> str:
        """
        Uploads a local file to a remote storage location.

        Args:
            local_path (str): The path to the local file to be uploaded.
            remote_path (str): The path where the file should be stored remotely.

        Returns:
            str: The URL of the uploaded file in the remote storage.
        """
        azure_file = self.storage_container.create_file(remote_path)
        with open(local_path, 'rb') as file_stream:
            azure_file.upload(file_stream.read())
        remote_url = azure_file.get_remote_url()
        return remote_url

    def download_remote_file(self, remote_path: str, local_path: str) -> str:
        """
        Downloads a file from a remote storage location to a local path.
        Args:
            remote_path (str): The path to the remote file to be downloaded.
            local_path (str): The local path where the file should be saved.
        Returns:
            str: The local path where the file has been saved.
        """
        #  Change this to download from client
        file_entity = self.storage_client.get_file_from_url(self.config.storage_container_name, remote_path)
        
        with open(local_path, 'wb') as file_stream:
            file_stream.write(file_entity.get_stream())

        return ''