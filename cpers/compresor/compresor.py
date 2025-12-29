from abc import ABC, abstractmethod
class Compresor:
    def __init__(self, video_path, apsect_ratio, media_social_type):
        self.video_path = video_path
        self.apsect_ratio = apsect_ratio
        self.media_social_type = media_social_type
        
    @abstractmethod(ABC)
    def compress(self):
        pass
    
    @abstractmethod(ABC)
    def media_social(self):
        pass