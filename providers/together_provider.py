# providers/together_provider.py
from typing import List
from together import Together
from .base import ImageProvider

_DEFAULT_MODEL = "black-forest-labs/FLUX.1-dev"

class TogetherImageProvider(ImageProvider):
    """
    Together Images API (FLUX family).
    Docs: https://docs.together.ai/docs/images-overview
          https://docs.together.ai/reference/images
    """
    def __init__(self, api_key: str, model: str = _DEFAULT_MODEL):
        # The SDK reads TOGETHER_API_KEY from env automatically,
        # but we also pass it explicitly to be safe.
        self.client = Together(api_key=api_key)
        self.model = model

    def generate_image(self, prompt: str, size: str = "1024x1024", n: int = 1) -> List[str]:
        width, height = (int(x) for x in size.split("x"))
        # steps 24–30 are a good sweet spot for interiors; dev is fast, pro is premium.
        resp = self.client.images.generate(
            prompt=prompt,
            model=self.model,
            width=width,
            height=height,
            steps=28,
            n=n,
            response_format="b64_json",  # return base64 in JSON
        )
        # Each item exposes .b64_json
        return [d.b64_json for d in resp.data]
