from app.services.IDownloadService import IDownloadService


class DownloadController:
    
    def __init__(self, download_service: IDownloadService):
        self.download_service = download_service
