from typing import Dict

STYLE_PRESETS: Dict[str, str] = {
    "Scandinavian": "Scandinavian, clean lines, natural light, light oak wood, soft neutrals",
    "Minimalist": "Minimalist, uncluttered, functional, neutral palette, simple geometric forms",
    "Industrial": "Industrial, exposed brick, concrete, metal accents, darker palette, loft vibe",
    "Japandi": "Japandi, warm minimalism, natural materials, low furniture, earthy tones",
    "Boho": "Bohemian, eclectic textiles, plants, layered textures, warm inviting colors",
    "Sali": "No windows, futuristic lights, modern furniture"
}

NEGATIVE_CLAUSES = (
    "No people, no text, no logos, no watermarks, no deformed geometry, "
    "physically plausible lighting and materials."
)

def compose_prompt(
    style: str,
    room_type: str,
    elements: str,
    materials: str,
    palette: str,
    lighting: str,
    camera: str,
    extra: str = ""
) -> str:
    style_desc = STYLE_PRESETS.get(style, style)
    parts = [
        f"Photorealistic {room_type} interior visualization.",
        f"Style: {style_desc}.",
        f"Key elements: {elements}.",
        f"Materials: {materials}.",
        f"Color palette: {palette}.",
        f"Lighting: {lighting}.",
        f"Camera/framing: {camera}.",
    ]
    if extra.strip():
        parts.append(f"Extras: {extra.strip()}.")
    parts.append(NEGATIVE_CLAUSES)
    parts.append("High detail, realistic furniture layout, natural proportions, interior design render quality.")
    return " ".join(parts)
