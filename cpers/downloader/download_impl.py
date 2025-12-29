import yt_dlp
import os
from downloader.base import Downloader
from logger import logger
class DownloadImpl(Downloader):
    
    def _progress_hook(self, d):
        if d['status'] == 'downloading':
            percent = d.get('_percent_str', 'N/A').strip()
            speed = d.get('_speed_str', 'N/A').strip()
            eta = d.get('_eta_str', 'N/A').strip()
            logger.info(f"[Downloader] Downloading... {percent} at {speed}, ETA: {eta}")
        elif d['status'] == 'finished':
            logger.info(f"[Downloader] Download finished, now post-processing...")
    
    def download(self, url:str) -> str:
        os.makedirs(self.download_path, exist_ok=True )
        with yt_dlp.YoutubeDL({"quiet": True}) as ydl:
            info = ydl.extract_info(url, download=False)
        
        video_id = info["id"]
        ext = "mp4"
        output_file = os.path.join(self.download_path, f"{video_id}.{ext}")
        
        if os.path.exists(output_file):
            print(f"[Downloader] File already exists: {output_file}")
            return output_file
        
        ydl_opts = {
            **self.ydl_opts,
            "outtmpl": output_file,
            "format": "mp4",
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        # logging
        print(f"[Downloader] Downloaded video to: {output_file}")
        return output_file