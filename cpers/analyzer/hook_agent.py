from analyzer.base import Analyzer
from agents.ollama_client import OllamaClient
import json
from logger import logger

class HookAgent(Analyzer):
    def __init__(self, ollama: OllamaClient):
        self.ollama = ollama
        
    def process(self, review:dict)->dict:
        prompt = f"""
kamu adalah short-from video strategist profesional.property

Dari data berikut, pilih 1 hook terbaik untuk video pendek.property

Kriteria:
- Stop scrolling
- Kalimat kuat di awal
- Durasi 20-30 detik
- Satu ide utuh

Output HARUS JSON:
{{
    "hook_text": "...",
    "start": 0.0,
    "endt": 0.0
    "reason": "..."
}}

Data:
{json.dumps(review, indent=2)}
"""
        raw = self.ollama.generate(prompt)
        try:
            logger.info(f"Model response: {raw}")
            result = json.loads(raw)
        except json.JSONDecodeError:
            logger.error(f"Failed to parse JSON from model response: {raw}")
            raise ValueError("Failed to parse JSON from model response")
        return result