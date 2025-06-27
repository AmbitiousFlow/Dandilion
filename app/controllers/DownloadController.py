from app.services.IDownloadService import IDownloadService
from PySide6.QtWidgets import QFileDialog


class DownloadController:
    """
    Controller for managing media downloads.
    This class interacts with the IDownloadService to perform download operations.
    Attributes:
        download_service (IDownloadService): An instance of a service that implements IDownloadService.
    """

    def __init__(self, download_service: IDownloadService):
        self.download_service = download_service
        self.destination = "."

    def download(self, url: str, format: str = "MP3", destination: str = ".") -> None:
        """
        Initiates the download of a media file.
        :param url: The URL of the media file to download.
        :param format: The format in which to download the media (default is 'MP3').
        :param destination: The local path where the file should be saved (default is current directory).
        """

        self.download_service.download(url, format, destination)

    def set_path(self):
        dialog = QFileDialog.getExistingDirectory(
            None, "Select Download Directory", "."
        )
        if dialog:
            self.destination = dialog
        else:
            return None
        
    def get_path(self):
        return self.destination