from yt_dlp.utils import DownloadError
from yt_dlp import YoutubeDL
from customtkinter import CTkTextbox, CTkProgressBar


class DownloadService:

    def __init__(self , progress_bar: CTkProgressBar=None , output_area: CTkTextbox=None):
        self.progress_bar = progress_bar
        self.output_area  = output_area

    def on_progress(
        self, info_dict:dict
    ): 
        file        = info_dict.get('filname', 'Unknown')
        downloaded  = info_dict.get('downloaded_bytes', 0)
        total       = info_dict.get('total_bytes', 0)

        if total:
            percent = int((downloaded / total) * 100)
            self.progress_bar.set(float(percent) / 100)
            self.output_area.insert("end", f"Downloading {file}: {downloaded}/{total} bytes ({percent:.2f}%)\n")
            
    def download(self, url: str, path: str):
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
                "format": "bestaudio/best",
                "extractaudio": True,
                "audioformat": "mp3",
                "ffmpeg_location": "app/bin/ffmpeg.exe",
                "progress_hooks": [self.on_progress],
                "postprocessors": [
                    {
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": "mp3",
                        "preferredquality": "0",
                    }
                ],
            }
            with YoutubeDL(self.ydl_opts) as youtubeClient:
                streamed_file = youtubeClient.download(url)

            return {"file": streamed_file}

        except DownloadError as e:
            return {"error": str(e)}


