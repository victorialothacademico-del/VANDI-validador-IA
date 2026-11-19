"""Identidade visual da VANDI — Validador Automatizado de Documentação
para Incorporação de Redes de Distribuição.

Uso no app.py:
    from vandi_theme import aplicar_tema, cabecalho, etapas, FAVICON
    st.set_page_config(page_title="VANDI", page_icon=FAVICON, layout="wide")
    aplicar_tema()
    cabecalho()
"""
import base64
from pathlib import Path

import streamlit as st

BASE = Path(__file__).parent
LOGO = BASE / "assets" / "vandi_logo.png"
FAVICON = str(BASE / "assets" / "favicon.png") if (BASE / "assets" / "favicon.png").exists() else "🔷"

# Paleta extraída do logo
AZUL = "#16436D"        # azul marinho (logo)
AZUL_ESCURO = "#0E2F4F"
AZUL_CLARO = "#2F6FA8"
FUNDO = "#F4F7FB"
BORDA = "#DCE4EE"
TEXTO = "#1B2A3A"
TEXTO_SUAVE = "#5B6B7D"


def _logo_b64() -> str:
    if LOGO.exists():
        return base64.b64encode(LOGO.read_bytes()).decode()
    return ""


CSS = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700;800&family=Inter:wght@400;500;600&display=swap');

html, body, [class*="css"], .stApp {{ font-family: 'Inter', 'Source Sans Pro', sans-serif; color: {TEXTO}; }}
.stApp {{ background: {FUNDO}; }}

/* esconde o menu/rodapé padrão do Streamlit */
#MainMenu, footer {{ visibility: hidden; }}
header[data-testid="stHeader"] {{ background: transparent; }}

/* largura de leitura confortável */
.block-container {{ max-width: 1120px; padding-top: 1.2rem; padding-bottom: 4rem; }}

/* ---------- cabeçalho ---------- */
.vandi-header {{
    background: #FFFFFF; border: 1px solid {BORDA}; border-top: 5px solid {AZUL};
    border-radius: 14px; padding: 1.1rem 1.6rem; margin-bottom: 1.1rem;
    display: flex; align-items: center; gap: 1.5rem; flex-wrap: wrap;
    box-shadow: 0 2px 10px rgba(22,67,109,.06);
}}
.vandi-header img {{ height: 52px; width: auto; }}
.vandi-wordmark {{ font-family: 'Montserrat', sans-serif; font-weight: 800; font-size: 2.2rem; color: {AZUL}; letter-spacing: .02em; }}
.vandi-sep {{ width: 1px; align-self: stretch; background: {BORDA}; }}
.vandi-titulo {{ flex: 1; min-width: 240px; }}
.vandi-titulo b {{ display:block; font-family:'Montserrat',sans-serif; font-size: .98rem; color: {AZUL_ESCURO}; line-height:1.25; }}
.vandi-chip {{
    background: #EAF1F9; color: {AZUL}; border: 1px solid {BORDA}; border-radius: 999px;
    padding: .28rem .8rem; font-size: .76rem; font-weight: 600; white-space: nowrap;
}}
@media (max-width: 640px) {{ .vandi-sep {{ display:none; }} .vandi-header img {{ height: 40px; }} }}

/* ---------- títulos ---------- */
h1, h2, h3, h4 {{ font-family: 'Montserrat', sans-serif !important; color: {AZUL_ESCURO} !important; letter-spacing: -.01em; }}
h2 {{ font-size: 1.35rem !important; }}
h3 {{ font-size: 1.1rem !important; }}

/* ---------- navegação (container key="nav") ---------- */
.st-key-nav div[role="radiogroup"] {{
    background: #FFFFFF; border: 1px solid {BORDA}; border-radius: 12px; padding: .3rem; gap: .3rem; width: fit-content;
}}
.st-key-nav div[role="radiogroup"] label {{
    padding: .45rem 1.1rem; border-radius: 9px; margin: 0; cursor: pointer; transition: background .15s;
}}
.st-key-nav div[role="radiogroup"] label > div:first-child {{ display: none; }}   /* esconde a bolinha */
.st-key-nav div[role="radiogroup"] label p {{ font-weight: 600; color: {TEXTO_SUAVE}; }}
.st-key-nav div[role="radiogroup"] label:hover {{ background: #EAF1F9; }}
.st-key-nav div[role="radiogroup"] label:has(input:checked) {{ background: {AZUL}; }}
.st-key-nav div[role="radiogroup"] label:has(input:checked) p {{ color: #FFFFFF; }}

/* ---------- etapas ---------- */
.vandi-etapas {{ display:flex; gap:.6rem; margin: .4rem 0 1.2rem; flex-wrap: wrap; }}
.vandi-etapa {{
    display:flex; align-items:center; gap:.5rem; font-size:.85rem; font-weight:600; color:{TEXTO_SUAVE};
    background:#FFFFFF; border:1px solid {BORDA}; border-radius:999px; padding:.3rem .9rem .3rem .35rem;
}}
.vandi-etapa i {{
    font-style:normal; width:1.5rem; height:1.5rem; border-radius:50%; display:grid; place-items:center;
    background:{BORDA}; color:{TEXTO_SUAVE}; font-size:.78rem;
}}
.vandi-etapa.ativa {{ color:{AZUL}; border-color:{AZUL}; }}
.vandi-etapa.ativa i {{ background:{AZUL}; color:#FFFFFF; }}
.vandi-etapa.feita i {{ background:{AZUL_CLARO}; color:#FFFFFF; }}

/* ---------- cartões, formulários, campos ---------- */
[data-testid="stForm"] {{
    background:#FFFFFF; border:1px solid {BORDA}; border-radius:14px; padding:1.4rem 1.6rem;
