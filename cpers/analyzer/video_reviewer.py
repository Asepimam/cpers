from analyzer.base import Analyzer
from agents.ollama_client import OllamaClient
from logger import logger
import json, re
import utils.extrac_json as json_extractor
class VideoReviewer(Analyzer):
    def __init__(self, ollama: OllamaClient):
        self.ollama = ollama
        
    def process(self, transcript: dict) -> dict:
        prompt = f"""
        Kamu adalah video reviewer profesional.

        ATURAN KERAS:
        - Output HARUS HANYA JSON
        - TANPA penjelasan
        - TANPA markdown
        - TANPA komentar
        - TANPA teks tambahan

        Format JSON WAJIB:
        {{
        "topic": "string",
        "conversation": [
            {{ "text": "string", "start": number, "end": number }}
        ],
        "key_moments": [
            {{ "type": "hook|insight|climax", "start": number, "end": number }}
        ]
        }}

        Transkrip:
        {json.dumps(transcript, ensure_ascii=False)}
        """

        raw = self.ollama.chat([
            {"role": "user", "content": prompt}
        ])
        try:
            logger.info(f"Model response: {raw}")
            result = json_extractor.extract_json(raw)
            return result
        except Exception as e:
            logger.error(f"Failed to parse JSON from model response: {raw}")
            raise ValueError("Failed to parse JSON from model response ")
        return result
