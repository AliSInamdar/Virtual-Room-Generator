import base64
import io
import os
from dataclasses import dataclass
from typing import Optional, List

from dotenv import load_dotenv
import streamlit as st

from providers.openai_provider import OpenAIImageProvider
from utils.prompt_templates import STYLE_PRESETS, compose_prompt

load_dotenv()

@dataclass
class GenOptions:
    style: str
    room_type: str
    elements: str
    materials: str
    palette: str
    lighting: str
    camera: str
    size: str
    variations: int

def init_state():
    if "gallery" not in st.session_state:
        st.session_state.gallery = []

def decode_b64_to_bytes(b64: str) -> bytes:
    return base64.b64decode(b64)

def main():
    st.set_page_config(page_title="RoomGen — Text → Furnished Room", page_icon="🛋️", layout="wide")
    init_state()

    st.title("🛋️ RoomGen")
    st.caption("Type a description → get a photorealistic, fully furnished room image.")

    # Sidebar: provider + settings
    with st.sidebar:
        st.subheader("⚙️ Settings")
        provider_name = st.selectbox("Image Provider", ["Together (FLUX)","OpenAI (recommended)"], index=0)
        size = st.selectbox("Image Size", ["1024x1024", "768x768", "512x512"], index=0)
        variations = st.slider("Number of Variations", 1, 2, 1)
        st.markdown("---")
        st.caption("Set your API key in `.env` or in this box (overrides env).")
        openai_key_override = st.text_input("OPENAI_API_KEY", type="password")

    # Prompt composer
    st.subheader("📝 Describe your room")
    col1, col2 = st.columns([1,1])
    with col1:
        style = st.selectbox("Style preset", list(STYLE_PRESETS.keys()), index=0)
        room_type = st.selectbox(
            "Room type",
            ["living room", "bedroom", "kitchen", "home office", "dining room", "bathroom", "kids room"],
            index=0
        )
        elements = st.text_input("Key elements", "sofa, coffee table, area rug, wall art, floor lamp")
        materials = st.text_input("Materials", "light oak wood, linen upholstery, matte black metal")
    with col2:
        palette = st.text_input("Color palette", "soft neutrals, sage green accents")
        lighting = st.text_input("Lighting", "soft ambient, warm temperature, window light")
        camera = st.text_input("Camera / framing", "35mm lens, eye-level, centered composition")

    # Free-form addition / override
    extra_desc = st.text_area("Extra description (optional)", "", help="Add anything special (e.g., bay windows, bookshelves, plants).")

    # Compose final prompt preview
    final_prompt = compose_prompt(
        style=style,
        room_type=room_type,
        elements=elements,
        materials=materials,
        palette=palette,
        lighting=lighting,
        camera=camera,
        extra=extra_desc
    )

    with st.expander("🔍 Final prompt (what the model sees)"):
        st.code(final_prompt)

    # Generate
    do_gen = st.button("✨ Generate", type="primary")

    if do_gen:
        try:
            if provider_name.startswith("Together"):
                key = os.getenv("TOGETHER_API_KEY", "")
                if not key:
                    st.error("Missing TOGETHER_API_KEY. Add it to .env or your environment.")
                    st.stop()
                from providers.together_provider import TogetherImageProvider
                provider = TogetherImageProvider(api_key=key)
            elif provider_name.startswith("OpenAI"):
                key = openai_key_override or os.getenv("OPENAI_API_KEY", "")
                if not key:
                    st.error("Missing OPENAI_API_KEY.")
                    st.stop()
                provider = OpenAIImageProvider(api_key=key)
            else:
                st.error("Unknown provider selected.")
                st.stop()   

            with st.spinner("Creating your room…"):
                images_b64: List[str] = provider.generate_image(
                    prompt=final_prompt,
                    size=size,
                    n=variations
                )

            cols = st.columns(variations)
            for i, img_b64 in enumerate(images_b64):
                img_bytes = decode_b64_to_bytes(img_b64)
                cols[i].image(img_bytes, caption=f"Result {i+1} — {size}")
                # Save to gallery
                st.session_state.gallery.insert(0, {"bytes": img_bytes, "size": size, "style": style, "room_type": room_type, "prompt": final_prompt})

                # Download button
                cols[i].download_button(
                    "Download PNG",
                    data=img_bytes,
                    file_name=f"roomgen_{style}_{room_type}_{i+1}.png",
                    mime="image/png",
                    use_container_width=True
                )

        except Exception as e:
            st.error(f"Generation failed: {e}")

    # Gallery
    if st.session_state.gallery:
        st.subheader("🖼️ Recent Generations")
        grid_cols = st.columns(3)
        for idx, item in enumerate(st.session_state.gallery[:6]):
            col = grid_cols[idx % 3]
            col.image(item["bytes"], caption=f'{item["style"]} {item["room_type"]}')
            with col.expander("Prompt"):
                col.code(item["prompt"])

    st.markdown("---")
    st.caption("Tip: start simple. You can add windows, wall colors, ceiling lights, rugs, etc., in the extra box.")

if __name__ == "__main__":
    main()
