import ollama
from typing import List, Dict

class OllamaClient:
    def __init__(self, model: str = "llama3.1"):
        self.model = model

    def chat(self, messages: List[Dict[str, str]]) -> str:
        try:
            response = ollama.chat(
                model=self.model,
                messages=messages,
            )
            return response["message"]["content"]
        except Exception as e:
            raise RuntimeError(f"Ollama error: {e}")
