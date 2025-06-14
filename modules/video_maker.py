from __future__ import annotations

import logging
from typing import List

from moviepy.editor import (AudioFileClip, ImageClip, VideoFileClip,
                            concatenate_videoclips)

logger = logging.getLogger(__name__)


def create_scene_video(frame_paths: List[str], audio_path: str, output_path: str, fps: int = 1) -> str:
    """Create a video clip for a scene from frames and audio."""
    clips = [ImageClip(fp).set_duration(3) for fp in frame_paths]
    video = concatenate_videoclips(clips)
    if audio_path:
        audio = AudioFileClip(audio_path)
        video = video.set_audio(audio)
    video.write_videofile(output_path, fps=fps, verbose=False, logger=None)
    logger.debug("Created scene video %s", output_path)
    return output_path


def assemble_video(scene_videos: List[str], output_path: str) -> str:
    """Concatenate scene videos into final video."""
    clips = [VideoFileClip(v) for v in scene_videos]
    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile(output_path, verbose=False, logger=None)
    logger.debug("Assembled final video %s", output_path)
    return output_path
