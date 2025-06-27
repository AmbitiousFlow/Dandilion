from app.services.IDownloadService import IDownloadService
from PySide6.QtWidgets import QWidget
from app.models.Media import Media
from yt_dlp import YoutubeDL
import uuid
import os

from app.utils.download import download_audio , download_video

class DownloadService(IDownloadService):

    def download(self, url: str, format:str = 'MP3' , destination: str = ".") -> None:
        """
        Downloads a file from the given URL to the specified destination.
        :param url: The URL of the file to download.
        :param destination: The local path where the file should be saved.
        """

        media = Media(url=url, format=format)

        if format not in ['MP3', 'MP4']:
            raise ValueError("Unsupported format. Use 'MP3' or 'MP4'.")

        if format == 'MP3':
            download_audio(url=media.url)

        else:
            download_video(url=media.url)


    def download_with_progress(self, url: str, destination: str , widget : QWidget) -> None:
        """
        Downloads a file from the given URL to the specified destination with progress tracking.
        :param url: The URL of the file to download.
        :param destination: The local path where the file should be saved.
        """
        pass
