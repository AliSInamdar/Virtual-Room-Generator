from abc import ABC, abstractmethod
from typing import List

class ImageProvider(ABC):
    @abstractmethod
    def generate_image(self, prompt: str, size: str = "1024x1024", n: int = 1) -> List[str]:
        """Return a list of base64-encoded PNGs."""
        raise NotImplementedError
