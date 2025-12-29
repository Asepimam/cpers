from analyzer.base import Analyzer
from faster_whisper import WhisperModel
from logger import logger
class Transcriber(Analyzer):
    
    def __init__(self, model_size:str="base"):
        self.model = WhisperModel(model_size)
        
        
    def process(self, video_path:str)->dict:
        
        segments, _ = self.model.transcribe(video_path)
        
        transcript = []
        for segment in segments:
            transcript.append({
                "start": segment.start,
                "end": segment.end,
                "text": segment.text
            })
            logger.info(f"[Transcriber] Transcribed segment from {segment.start} to {segment.end}: {segment.text}")
        return {
            "segments": transcript
        }