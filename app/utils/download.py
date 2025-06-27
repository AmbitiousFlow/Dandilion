from yt_dlp import YoutubeDL

import os

current_dir = os.path.dirname(__file__)

ffmpeg_path = os.path.abspath(os.path.join(current_dir, '..', 'libs', 'ffmpeg', 'bin', 'ffmpeg.exe'))


def download_video(url : str): 
    
    yt = YoutubeDL()
    yt.download([url])

def download_audio(url: str):

    options = {
        "format": "bestaudio/best",
        "outtmpl": "%(title)s.%(ext)s",
        "ffmpeg_location": ffmpeg_path,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
        "quiet": False,
        "noplaylist": True,
    }

    with YoutubeDL(options) as ydl:
        ydl.download(url)