import subprocess
from analyzer.base import Analyzer
import os
from logger import logger

class CutterAgent(Analyzer):
    
    def process(self, video_path:str, start_time:float, end_time:float, output_path:str) -> str:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        command = [
            "ffmpeg",
            "-y",
            "-i", video_path,
            "-ss", str(start_time),
            "-to", str(end_time),
            "-c", "copy",
            output_path
        ]
        
        subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        logger.info(f"[CutterAgent] Cut video from {start_time} to {end_time} into {output_path}")
        return output_path