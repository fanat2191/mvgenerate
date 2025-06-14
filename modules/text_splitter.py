from __future__ import annotations

import json
import logging
from typing import List, Dict

import openai

from config import OPENAI_API_KEY

logger = logging.getLogger(__name__)
openai.api_key = OPENAI_API_KEY

PROMPT_TEMPLATE = (
    "Разбей следующий текст на логические сцены. "
    "Верни список JSON объектов с ключами: location, characters, actions, mood, dialogue."
)


def split_text(text: str) -> List[Dict[str, str]]:
    """Use LLM to split text into scene descriptions."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": PROMPT_TEMPLATE},
                {"role": "user", "content": text},
            ],
            max_tokens=1000,
        )
        content = response.choices[0].message["content"]
        scenes = json.loads(content)
        logger.debug("Received scenes: %s", scenes)
        return scenes
    except Exception as exc:
        logger.error("Failed to split text: %s", exc)
        return []
