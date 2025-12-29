from downloader.download_impl import DownloadImpl
from analyzer.transcriber import Transcriber
from analyzer.video_reviewer import VideoReviewer
from analyzer.cutter_agent import CutterAgent
from analyzer.hook_agent import HookAgent
from analyzer.subtitle_agent import SubtitleAgent
from agents.ollama_client import OllamaClient
from logger import logger
import os

def main():
    ydl_opts = {"noplaylist": True}

    downloader = DownloadImpl(
        ydl_opts=ydl_opts,
        download_path="./downloads"
    )

    url = input("Enter the video URL to download: ")

    file_path = downloader.download(url)
    logger.info(f"[Main] Video path: {file_path}")

    # 1️⃣ Transcribe
    transcriber = Transcriber()
    transcript = transcriber.process(file_path)

    # 2️⃣ Init shared LLM
    ollama = OllamaClient(model="llama3.1")

    # 3️⃣ Review video
    reviewer = VideoReviewer(ollama)
    review = reviewer.process(transcript)

    # 4️⃣ Find hooks
    hook_agent = HookAgent(ollama)
    hooks = hook_agent.process(review)

    # 5️⃣ Cut & subtitle
    cutter = CutterAgent()
    subtitle_agent = SubtitleAgent()

    os.makedirs("outputs", exist_ok=True)

    for i, h in enumerate(hooks, start=1):
        logger.info(f"[Main] Processing clip {i}/{len(hooks)}")

        clip_path = cutter.process(
            file_path,
            h["start"],
            h["end"],
            f"outputs/clip_{i}.mp4"
        )

        # ⬅️ subtitle HARUS dari transcript asli
        subtitle_agent.process(
            transcript,
            h["start"],
            h["end"],
            f"outputs/clip_{i}.srt"
        )

if __name__ == "__main__":
    main()
