import os
from typing import List

from openai import OpenAI
from .base import ImageProvider

_OPENAI_IMAGE_MODEL = os.getenv("OPENAI_IMAGE_MODEL", "gpt-image-1")

class OpenAIImageProvider(ImageProvider):
    def __init__(self, api_key: str):
        # The SDK reads key from env, but we allow explicit injection too.
        os.environ["OPENAI_API_KEY"] = api_key
        self.client = OpenAI()

    def generate_image(self, prompt: str, size: str = "1024x1024", n: int = 1) -> List[str]:
        # OpenAI returns base64 JSON for images
        resp = self.client.images.generate(
            model=_OPENAI_IMAGE_MODEL,
            prompt=prompt,
            size=size,
            n=n
        )
        # Each item has .b64_json
        images_b64 = [d.b64_json for d in resp.data]
        return images_b64
