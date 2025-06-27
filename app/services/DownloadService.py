from app.services.IDownloadService import IDownloadService
from PySide6.QtWidgets import QWidget , QProgressBar , QApplication
from app.models.Media import Media
from yt_dlp import YoutubeDL
import uuid
import os
from typing import Optional

from app.utils.download import download_audio, download_video


class DownloadService(IDownloadService):
    """Service for downloading media files in MP3 or MP4 format with optional progress tracking."""

    SUPPORTED_FORMATS = {"MP3", "MP4"}

    def download(self, url: str, format: str = "MP3", destination: str = ".") -> None:
        """
        Download a file from the given URL to the specified destination.

        Args:
            url: The URL of the file to download.
            format: The media format ('MP3' or 'MP4'). Defaults to 'MP3'.
            destination: The local path where the file should be saved. Defaults to current directory.
        Raises:
            ValueError: If the specified format is not supported.
        """
        self._validate_format(format)
        media = Media(url=url, format=format)
        self._download_media(media, destination)

    def download_with_progress(
        self, url: str, destination: str, widget: QWidget, format: str = "MP3"
    ) -> None:
        """
        Download a file with progress tracking displayed on a QWidget.

        Args:
            url: The URL of the file to download.
            destination: The local path where the file should be saved.
            widget: The QWidget to update with download progress.
            format: The media format ('MP3' or 'MP4'). Defaults to 'MP3'.
        Raises:
            ValueError: If the specified format is not supported or widget is invalid.
        """
        self._validate_format(format)
        if not isinstance(widget, QProgressBar):
            raise ValueError("Widget must be a QProgressBar for progress tracking")
        media = Media(url=url, format=format)
        progress_callback = self._create_progress_callback(widget)
        self._download_media(media, destination, progress_callback)

    def _validate_format(self, format: str) -> None:
        """Validate that the provided format is supported.

        Args:
            format: The media format to validate.
        Raises:
            ValueError: If the format is not in SUPPORTED_FORMATS.
        """
        if format not in self.SUPPORTED_FORMATS:
            raise ValueError(f"Unsupported format. Use one of {self.SUPPORTED_FORMATS}.")

    def _download_media(
        self, media: Media, destination: str, callback: Optional[callable] = None
    ) -> None:
        """Download media based on its format.

        Args:
            media: The Media object containing URL and format.
            destination: The local path where the file should be saved.
            callback: Optional callback function for progress updates.
        """
        download_func = download_audio if media.format == "MP3" else download_video
        download_func(url=media.url, destination=destination, callback=callback)

    def _create_progress_callback(self, widget: QProgressBar) -> callable:
        """Create a callback function for tracking download progress.

        Args:
            widget: The QProgressBar to update with progress.
        Returns:
            A callback function that updates the progress bar's value.
        """
        def progress_hook(d):
            if d["status"] == "downloading":
                percent = (d.get("downloaded_bytes", 0) / d.get("total_bytes", 1)) * 100
                self._update_widget_progress(widget, percent)
            elif d["status"] == "finished":
                self._update_widget_progress(widget, 100)

        return progress_hook

    def _update_widget_progress(self, widget: QProgressBar, percent: float) -> None:
        """Update the progress bar's value and refresh the UI.

        Args:
            widget: The QProgressBar to update.
            percent: The progress percentage to set (0-100).
        """
        widget.setValue(int(percent))
        QApplication.processEvents()  # Force UI update to prevent freezing