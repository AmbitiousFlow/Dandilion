from abc import ABC

class DownloadServiceAbstract(ABC):
    
    def on_progress(self) -> None:
        ...

    def download(self) -> None:
        ...