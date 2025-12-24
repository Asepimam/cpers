from abc import ABC, abstractmethod

class Downloader:
    def __init__(self, ydl_opts:object, download_path:str ):
        self.ydl_opts = ydl_opts 
        self.download_path = download_path
    @abstractmethod(ABC)    
    def download(self, url:str, donwload_path:str):
        pass