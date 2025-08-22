# 🛋️ Virtual Room Generator

Transform **text descriptions** into **photorealistic, fully furnished room designs**.  
Built with **Streamlit** and powered by **Together AI’s FLUX models**.

---

## ✨ Features
- 📝 **Prompt-based generation** — Describe your dream room in natural language.
- 🎨 **Style presets** — Scandinavian, Minimalist, Japandi, Industrial, Boho.
- 📐 **Flexible controls** — Room type, materials, palette, lighting, camera angle.
- 🖼️ **Image gallery** — View your last few generations in-app.
- 💾 **Downloadable results** — Save renders as PNG instantly.
- 🔌 **Pluggable providers** — Currently uses Together AI (FLUX.1-dev), with OpenAI support optional.

---

## 🚀 Demo

_(Add screenshot / GIF here once deployed)_

---

## ⚙️ Installation

Clone the repo and set up dependencies:

```bash
git clone https://github.com/<your-username>/Virtual-Room-Generator.git
cd Virtual-Room-Generator

# Create venv
python3 -m venv .venv
source .venv/bin/activate   # Mac/Linux
# .venv\Scripts\activate    # Windows

# Install dependencies
pip install -r requirements.txt
```

🔑 API Key Setup
```
You need a Together AI API key.

Sign up at Together AI
.

Create an API key from your dashboard.

Add it to your environment:

export TOGETHER_API_KEY=your_key_here


Or copy .env.example to .env and fill in your key.
```
▶️ Usage
```
Run locally:

streamlit run app.py


Open your browser at http://localhost:8501
.
```
🌐 Deployment
```
Hugging Face Spaces

Create a new Space → Streamlit.

Push this repo.

Add your secret in Settings → Secrets:

TOGETHER_API_KEY=your_key_here

Streamlit Cloud

Go to share.streamlit.io
.

Link your repo.

Add your secret in App Settings → Secrets.
```
📁 Project Structure
```bash
Virtual-Room-Generator/
├─ app.py                  # Streamlit UI
├─ providers/              # Image provider wrappers
│   ├─ base.py
│   ├─ together_provider.py
│   └─ openai_provider.py  # optional
├─ utils/
│   ├─ prompt_templates.py # Style presets + prompt composer
├─ requirements.txt
├─ .env.example            # Sample env file
└─ README.md
```
🛠️ Tech Stack
```
Streamlit
 — Web UI

Together AI
 — Image generation (FLUX.1 models)

OpenAI
 (optional) — Alternative backend

Python-dotenv
 — Env management

📸 Example Prompts

“Scandinavian living room with oak floors, sage green sofa, soft ambient lighting, and wall art.”

“Industrial loft-style bedroom, exposed brick, dark palette, metal bedframe, warm lamps.”

“Japandi dining room, low furniture, earthy tones, natural wood, window lighting.”
```
⚠️ Notes

Keep your .env file private (never commit API keys).

If using OpenAI: gpt-image-1 requires verified org access.

Together API has rate limits; see docs
.

📜 License

MIT License © 2025 
```bash
Ali Inamdar
Sidharth Raj Khandelwal
```
