from abc import ABC, abstractmethod

class Downloader(ABC):
    def __init__(self, ydl_opts: dict, download_path: str):
        self.ydl_opts = ydl_opts
        self.download_path = download_path

    @abstractmethod
    def download(self, url: str) -> str:
        """Download video and return file path"""
        pass
