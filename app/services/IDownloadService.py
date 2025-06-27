from abc import ABC
from PySide6.QtWidgets import QWidget

class IDownloadService(ABC):
    
    def download(self, url: str, destination: str) -> None:
        """
        Downloads a file from the given URL to the specified destination.
        :param url: The URL of the file to download.
        :param destination: The local path where the file should be saved.
        """
        pass

    def download_with_progress(self, url: str, destination: str , widget : QWidget) -> None:
        """
        Downloads a file from the given URL to the specified destination with progress tracking.
        :param url: The URL of the file to download.
        :param destination: The local path where the file should be saved.
        """
        pass
