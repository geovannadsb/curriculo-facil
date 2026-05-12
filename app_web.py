import streamlit as st
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from curriculo import Curriculo
from gerador_pdf import gerar_pdf
from viacep import buscar_cidade_por_cep

# ── Configuração da página ───────────────────────────────────────────────────
st.set_page_config(
    page_title="CurrículoFácil",
    page_icon="📄",
    layout="centered",
)

# ── Estilo customizado (cores CEUB) ──────────────────────────────────────────
st.markdown("""
<style>
    .main { background-color: #f5f0f7; }
    .stButton>button {
        background-color: #662c92;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 8px 20px;
        font-weight: bold;
    }
    .stButton>button:hover { background-color: #43054e; }
    h1 { color: #43054e; }
    h2 { color: #662c92; border-bottom: 2px solid #bf0087; padding-bottom: 4px; }
</style>
""", unsafe_allow_html=True)

# ── Estado da sessão ─────────────────────────────────────────────────────────
if "curriculo" not in st.session_state:
    st.session_state.curriculo = Curriculo()

curriculo = st.session_state.curriculo

# ── Cabeçalho ────────────────────────────────────────────────────────────────
st.markdown("# 📄 CurrículoFácil")
st.markdown("Preencha seus dados e gere um currículo profissional em PDF com um clique.")
st.divider()

# ── Dados Pessoais ────────────────────────────────────────────────────────────
st.markdown("## 👤 Dados Pessoais")

col1, col2 = st.columns(2)
with col1:
    nome = st.text_input("Nome completo *", placeholder="Ex: Ana Silva")
    email = st.text_input("E-mail *", placeholder="Ex: ana@email.com")
with col2:
    telefone = st.text_input("Telefone", placeholder="Ex: 61999999999")
    cep = st.text_input("CEP", placeholder="Ex: 70040010")

cidade = st.text_input(
    "Cidade",
    value=st.session_state.get("cidade_cep", ""),
    placeholder="Será preenchida automaticamente pelo CEP",
)

if st.button("🔍 Buscar CEP"):
    try:
        resultado = buscar_cidade_por_cep(cep)
        st.session_state["cidade_cep"] = resultado
        st.success(f"Cidade encontrada: {resultado}")
        st.rerun()
    except Exception as e:
        st.error(str(e))

if st.button("💾 Salvar Dados Pessoais"):
    try:
        curriculo.adicionar_dados_pessoais(
            nome, email, telefone,
            st.session_state.get("cidade_cep", cidade)
        )
        st.success("✅ Dados pessoais salvos com sucesso!")
    except ValueError as e:
        st.error(str(e))

st.divider()

# ── Experiência Profissional ──────────────────────────────────────────────────
st.markdown("## 💼 Experiência Profissional")

col1, col2, col3 = st.columns(3)
with col1:
    empresa = st.text_input("Empresa *", placeholder="Ex: Google")
with col2:
    cargo = st.text_input("Cargo *", placeholder="Ex: Desenvolvedor")
with col3:
    periodo = st.text_input("Período", placeholder="Ex: 2022-2024")

if st.button("➕ Adicionar Experiência"):
    try:
        curriculo.adicionar_experiencia(empresa, cargo, periodo)
        st.success("✅ Experiência adicionada!")
    except ValueError as e:
        st.error(str(e))

if curriculo.experiencias:
    st.markdown("**Experiências adicionadas:**")
    for i, exp in enumerate(curriculo.experiencias):
        col1, col2 = st.columns([4, 1])
        with col1:
            st.markdown(f"- **{exp['cargo']}** @ {exp['empresa']} ({exp['periodo']})")
        with col2:
            if st.button("🗑️", key=f"del_exp_{i}"):
                curriculo.remover_experiencia(i)
                st.rerun()

st.divider()

# ── Formação Acadêmica ────────────────────────────────────────────────────────
st.markdown("## 🎓 Formação Acadêmica")

col1, col2, col3 = st.columns(3)
with col1:
    instituicao = st.text_input("Instituição *", placeholder="Ex: UnB")
with col2:
    curso = st.text_input("Curso *", placeholder="Ex: Ciência da Computação")
with col3:
    ano = st.text_input("Ano", placeholder="Ex: 2023")

if st.button("➕ Adicionar Formação"):
    try:
        curriculo.adicionar_formacao(instituicao, curso, ano)
        st.success("✅ Formação adicionada!")
    except ValueError as e:
        st.error(str(e))

if curriculo.formacoes:
    st.markdown("**Formações adicionadas:**")
    for i, form in enumerate(curriculo.formacoes):
        col1, col2 = st.columns([4, 1])
        with col1:
            st.markdown(f"- **{form['curso']}** - {form['instituicao']} ({form['ano']})")
        with col2:
            if st.button("🗑️", key=f"del_form_{i}"):
                curriculo.remover_formacao(i)
                st.rerun()

st.divider()

# ── Gerar PDF ────────────────────────────────────────────────────────────────
st.markdown("## 📄 Gerar Currículo em PDF")

if st.button("📄 Gerar PDF do Currículo", use_container_width=True):
    if not curriculo.esta_pronto():
        st.warning("⚠️ Preencha e salve os dados pessoais primeiro!")
    else:
        caminho = gerar_pdf(curriculo, "/tmp/curriculo_gerado.pdf")
        with open(caminho, "rb") as f:
            st.download_button(
                label="⬇️ Baixar PDF",
                data=f,
                file_name="curriculo.pdf",
                mime="application/pdf",
                use_container_width=True,
            )
        st.success("✅ PDF gerado! Clique em 'Baixar PDF' para salvar.")

st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:#999; font-size:12px;'>"
    "CurrículoFácil · Bootcamp II · CEUB 2026</p>",
    unsafe_allow_html=True,
)