from __future__ import annotations

import base64
from pathlib import Path

import streamlit as st


ROOT = Path(__file__).parent


def data_uri(path: Path) -> str:
    """Convierte una imagen local en un recurso autocontenido para el navegador."""
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:image/webp;base64,{encoded}"


def build_page() -> str:
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    css = (ROOT / "styles.css").read_text(encoding="utf-8")
    javascript = (ROOT / "script.js").read_text(encoding="utf-8")

    body = html.partition("<body>")[2].rpartition("</body>")[0]

    for image_path in sorted((ROOT / "assets").glob("*.webp")):
        relative_path = f"assets/{image_path.name}"
        embedded_image = data_uri(image_path)
        body = body.replace(relative_path, embedded_image)
        javascript = javascript.replace(relative_path, embedded_image)

    streamlit_shell_css = """
    [data-testid="stHeader"],
    [data-testid="stToolbar"],
    [data-testid="stDecoration"],
    [data-testid="stStatusWidget"] {
      display: none !important;
    }

    [data-testid="stAppViewContainer"],
    [data-testid="stMain"],
    .stMain,
    .stApp {
      background: var(--color-surface) !important;
    }

    [data-testid="stMainBlockContainer"],
    .block-container {
      width: 100% !important;
      max-width: none !important;
      padding: 0 !important;
      margin: 0 !important;
    }

    [data-testid="stAppViewContainer"] {
      overflow-x: hidden;
    }
    """

    return f"""
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600&family=Italiana&display=swap" rel="stylesheet">
    <style>{streamlit_shell_css}\n{css}</style>
    {body}
    <script>{javascript}</script>
    """


st.set_page_config(
    page_title="Nativa — Joyería con intención",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.html(build_page(), unsafe_allow_javascript=True)
