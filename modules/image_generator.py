from __future__ import annotations

import logging
import os
import uuid
from typing import List

logger = logging.getLogger(__name__)


def generate_images(prompt: str, output_dir: str) -> List[str]:
    """Placeholder image generation that creates empty image files."""
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, f"{uuid.uuid4()}.png")
    try:
        with open(path, "wb") as f:
            f.write(b"")
        logger.debug("Generated image for prompt '%s' at %s", prompt, path)
        return [path]
    except Exception as exc:
        logger.error("Failed to generate image: %s", exc)
        return []
