from analyzer.base import Analyzer
from logger import logger

class SubtitleAgent(Analyzer):
    def process(self, conversation: list , output_path: str):
        with open(output_path, 'w', encoding='utf-8') as f:
            for i, line in enumerate(conversation, start=1):
                f.write(f"{i}\n")
                f.write(f"{self._ts(line['start'])} --> {self._ts(line['end'])}\n")
                f.write(f"{line['text']}\n\n")  
                
        logger.info(f"[SubtitleAgent] Subtitle file created at: {output_path}")
    def _ts(self, seconds: float) -> str:
        ms = int((seconds  % 1) * 1000)
        s = int(seconds)
        h = s // 3600
        m = (s % 3600) // 60
        s = s % 60
        logger.debug(f"Converted {seconds} to timestamp {h:02}:{m:02}:{s:02},{ms:03}")
        return f"{h:02}:{m:02}:{s:02},{ms:03}"