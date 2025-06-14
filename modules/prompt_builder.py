from __future__ import annotations

import logging
from typing import Dict

logger = logging.getLogger(__name__)


def build_prompt(scene: Dict[str, str]) -> str:
    """Build image generation prompt for a scene."""
    try:
        location = scene.get("location", "")
        characters = ", ".join(scene.get("characters", [])) if isinstance(scene.get("characters"), list) else scene.get("characters", "")
        actions = scene.get("actions", "")
        mood = scene.get("mood", "")
        prompt = f"{mood} scene at {location} with {characters}. Actions: {actions}."
        logger.debug("Built prompt: %s", prompt)
        return prompt
    except Exception as exc:
        logger.error("Failed to build prompt: %s", exc)
        return ""
