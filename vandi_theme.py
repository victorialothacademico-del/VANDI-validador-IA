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
    box-shadow: 0 2px 10px rgba(22,67,109,.05);
}}
.stTextInput input, .stTextArea textarea, .stSelectbox [data-baseweb="select"] > div {{
    border-radius: 9px !important; border-color: {BORDA} !important; background:#FFFFFF !important;
}}
.stTextInput input:focus, .stTextArea textarea:focus {{ border-color:{AZUL} !important; box-shadow:0 0 0 1px {AZUL} !important; }}
[data-testid="stFileUploaderDropzone"] {{
    background:#FFFFFF; border:2px dashed {AZUL_CLARO}; border-radius:14px; padding:1.6rem;
}}

/* ---------- botões ---------- */
.stButton > button, .stFormSubmitButton > button, .stDownloadButton > button {{
    border-radius: 10px; font-weight: 600; padding: .55rem 1.3rem; border: 1px solid {AZUL}; transition: all .15s;
}}
.stButton > button[kind="primary"], .stFormSubmitButton > button[kind="primaryFormSubmit"], .stFormSubmitButton > button[kind="primary"] {{
    background: {AZUL}; color:#FFFFFF; border-color:{AZUL};
}}
.stButton > button[kind="primary"]:hover, .stFormSubmitButton > button:hover {{
    background:{AZUL_ESCURO}; border-color:{AZUL_ESCURO}; color:#FFFFFF;
}}
.stButton > button:disabled {{ background:{BORDA}; border-color:{BORDA}; color:{TEXTO_SUAVE}; }}
.stDownloadButton > button {{ background:#FFFFFF; color:{AZUL}; }}
.stDownloadButton > button:hover {{ background:#EAF1F9; }}

/* ---------- alertas e tabelas ---------- */
[data-testid="stAlert"] {{ border-radius: 12px; border: 1px solid {BORDA}; }}
[data-testid="stDataFrame"] {{ border:1px solid {BORDA}; border-radius:12px; overflow:hidden; }}
[data-testid="stExpander"] {{ background:#FFFFFF; border:1px solid {BORDA}; border-radius:12px; }}

/* ---------- barra lateral (administração) ---------- */
[data-testid="stSidebar"] {{ background:#FFFFFF; border-right:1px solid {BORDA}; }}
</style>
"""


def aplicar_tema():
    """Injeta o CSS da VANDI. Chamar logo após st.set_page_config()."""
    st.markdown(CSS, unsafe_allow_html=True)


def cabecalho(area: str | None = None):
    """Faixa superior com o logo e o nome por extenso. Se `area` for informada
    (ex.: "Área do analista"), mostra um selo à direita."""
    b64 = _logo_b64()
    logo = (f'<img src="data:image/png;base64,{b64}" alt="VANDI">' if b64
            else '<span class="vandi-wordmark">VANDI</span>')
    chip = f'<div class="vandi-chip">{area}</div>' if area else ""
    st.markdown(
        f"""
        <div class="vandi-header">
            {logo}
            <div class="vandi-sep"></div>
            <div class="vandi-titulo">
                <b>Validador Automatizado de Documentação<br>para Incorporação de Redes de Distribuição</b>
            </div>
            {chip}
        </div>
        """,
        unsafe_allow_html=True,
    )


def etapas(atual: int):
    """Indicador de progresso: 1 Cadastro · 2 Envio · 3 Resultado."""
    nomes = ["Cadastro", "Envio da documentação", "Resultado"]
    itens = []
    for i, nome in enumerate(nomes, start=1):
        cls = "ativa" if i == atual else ("feita" if i < atual else "")
        marca = "✓" if i < atual else str(i)
        itens.append(f'<div class="vandi-etapa {cls}"><i>{marca}</i>{nome}</div>')
    st.markdown(f'<div class="vandi-etapas">{"".join(itens)}</div>', unsafe_allow_html=True)
