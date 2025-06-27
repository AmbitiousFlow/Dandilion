from yt_dlp import YoutubeDL

def download_video(url : str): 
    
    yt = YoutubeDL()
    yt.download([url])

def download_audio(url: str):

    options = {
        "format": "bestaudio/best",
        "outtmpl": "%(title)s.%(ext)s",
        "ffmpeg_location": r"D:\\Work\\Dandilion\\bin\\ffmpeg.exe",
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