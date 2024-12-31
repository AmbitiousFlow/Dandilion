from .DownloadServiceAbstract import DownloadServiceAbstract
from PySide6.QtWidgets import QProgressBar
from PySide6.QtWidgets import QPlainTextEdit
from yt_dlp.utils import DownloadError
from yt_dlp import YoutubeDL

class DownloadService(DownloadServiceAbstract):
    
    def __init__(self , progress_bar:QProgressBar , output_text:QPlainTextEdit):
        super().__init__()
        self.progress_bar = progress_bar
        self.output_text  = output_text

    def on_progress(self , info_dict:dict):
        
        file        = info_dict.get('filname', 'Unknown')
        downloaded  = info_dict.get('downloaded_bytes', 0)
        total       = info_dict.get('total_bytes', 0)
        if total:
            percent = int((downloaded / total) * 100)
            self.progress_bar.setValue(percent)
            self.output_text.insertPlainText(f"Downloading {file}: {downloaded}/{total} bytes ({percent:.2f}%)\n")
    
    def download(self , url:str , path:str , type:str):
        """Downloads a video from youtube and extracts its audio
        into an mp3 file, saving it to the given path.

        Args:
            url (str): The url of the video to download.
            path (str): The path where the mp3 file will be saved.

        Returns:
            A dictionary containing either {"file": str} or {"error": str}.
            The "file" key is present when the download is successful, and
            contains the path of the saved mp3 file.
            The "error" key is present when the download fails, and contains
            the error message as a string.
        """
        try:
            self.ydl_opts = {
                "outtmpl": f"{path}/%(id)s.%(ext)s",
                "ffmpeg_location": "app/bin/ffmpeg.exe",
                "progress_hooks": [self.on_progress],
            }
            if type.lower() in ["mp3", "ogg", "wav"]:
                self.ydl_opts["extractaudio"] = True
                self.ydl_opts["audioformat"] = type
                self.ydl_opts["postprocessors"] = [
                    {
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": type,
                        "preferredquality": "0",
                    }
                ]
            elif type.lower() in ["mp4"]:
                self.ydl_opts["format"] = "best"

            # Use YoutubeDL to process the download
            with YoutubeDL(self.ydl_opts) as youtubeClient:
                streamed_file = youtubeClient.download([url])

            return {"file": streamed_file}

        except DownloadError as e:
            return {"error": str(e)}
