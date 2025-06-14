from __future__ import annotations

import argparse
import json
import logging
import os
import uuid
from typing import List

from config import AUDIO_DIR, FINAL_DIR, FRAMES_DIR, SCENES_DIR, VIDEO_DIR
from modules.image_generator import generate_images
from modules.prompt_builder import build_prompt
from modules.text_splitter import split_text
from modules.tts import generate_tts
from modules.video_maker import assemble_video, create_scene_video

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def process_text(text: str) -> str:
    if len(text) > 5000:
        raise ValueError("Input text exceeds 5000 characters")

    scenes = split_text(text)
    scene_file = os.path.join(SCENES_DIR, f"{uuid.uuid4()}.json")
    os.makedirs(SCENES_DIR, exist_ok=True)
    with open(scene_file, "w", encoding="utf-8") as f:
        json.dump(scenes, f, ensure_ascii=False, indent=2)
    logger.info("Scenes description saved to %s", scene_file)

    scene_videos: List[str] = []
    for idx, scene in enumerate(scenes):
        prompt = build_prompt(scene)
        frame_paths = generate_images(prompt, FRAMES_DIR)
        audio_path = os.path.join(AUDIO_DIR, f"scene_{idx}.wav")
        os.makedirs(AUDIO_DIR, exist_ok=True)
        generate_tts(scene.get("dialogue", ""), audio_path)

        video_path = os.path.join(VIDEO_DIR, f"scene_{idx}.mp4")
        os.makedirs(VIDEO_DIR, exist_ok=True)
        create_scene_video(frame_paths, audio_path, video_path)
        scene_videos.append(video_path)

    os.makedirs(FINAL_DIR, exist_ok=True)
    final_path = os.path.join(FINAL_DIR, "final.mp4")
    assemble_video(scene_videos, final_path)
    return final_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate video from text")
    parser.add_argument("input", help="Path to text file")
    args = parser.parse_args()

    with open(args.input, "r", encoding="utf-8") as f:
        text = f.read()

    try:
        final_video = process_text(text)
        logger.info("Final video created at %s", final_video)
    except Exception as exc:
        logger.error("Processing failed: %s", exc)


if __name__ == "__main__":
    main()
