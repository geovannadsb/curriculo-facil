import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from curriculo import Curriculo  # noqa: E402


# ── Dados Pessoais ────────────────────────────────────────────────────────────

def test_adicionar_dados_pessoais_validos():
    c = Curriculo()
    c.adicionar_dados_pessoais("Ana Silva", "ana@email.com", "61999999999", "Brasília")
    assert c.dados_pessoais["nome"] == "Ana Silva"
    assert c.dados_pessoais["email"] == "ana@email.com"


def test_dados_pessoais_sem_nome_levanta_erro():
    c = Curriculo()
    with pytest.raises(ValueError, match="Nome e e-mail são obrigatórios"):
        c.adicionar_dados_pessoais("", "ana@email.com", "", "")


def test_dados_pessoais_sem_email_levanta_erro():
    c = Curriculo()
    with pytest.raises(ValueError):
        c.adicionar_dados_pessoais("Ana Silva", "", "", "")


# ── Experiência ───────────────────────────────────────────────────────────────

def test_adicionar_experiencia_valida():
    c = Curriculo()
    c.adicionar_experiencia("Empresa X", "Desenvolvedor", "2022–2024")
    assert len(c.experiencias) == 1
    assert c.experiencias[0]["empresa"] == "Empresa X"


def test_adicionar_multiplas_experiencias():
    c = Curriculo()
    c.adicionar_experiencia("Empresa A", "Estagiário", "2020–2021")
    c.adicionar_experiencia("Empresa B", "Analista", "2021–2023")
    assert len(c.experiencias) == 2


def test_experiencia_sem_cargo_levanta_erro():
    c = Curriculo()
    with pytest.raises(ValueError):
        c.adicionar_experiencia("Empresa X", "", "2022–2024")


def test_experiencia_sem_empresa_levanta_erro():
    c = Curriculo()
    with pytest.raises(ValueError):
        c.adicionar_experiencia("", "Desenvolvedor", "2022–2024")


def test_remover_experiencia_valida():
    c = Curriculo()
    c.adicionar_experiencia("Empresa X", "Dev", "2022–2024")
    c.remover_experiencia(0)
    assert len(c.experiencias) == 0


def test_remover_experiencia_indice_invalido():
    c = Curriculo()
    with pytest.raises(IndexError):
        c.remover_experiencia(99)


# ── Formação ──────────────────────────────────────────────────────────────────

def test_adicionar_formacao_valida():
    c = Curriculo()
    c.adicionar_formacao("UnB", "Ciência da Computação", "2023")
    assert len(c.formacoes) == 1
    assert c.formacoes[0]["curso"] == "Ciência da Computação"


def test_formacao_sem_curso_levanta_erro():
    c = Curriculo()
    with pytest.raises(ValueError):
        c.adicionar_formacao("UnB", "", "2023")


def test_remover_formacao_indice_invalido():
    c = Curriculo()
    with pytest.raises(IndexError):
        c.remover_formacao(0)


# ── Estado geral ──────────────────────────────────────────────────────────────

def test_curriculo_nao_pronto_sem_dados():
    c = Curriculo()
    assert not c.esta_pronto()


def test_curriculo_pronto_com_dados():
    c = Curriculo()
    c.adicionar_dados_pessoais("João", "joao@email.com", "", "")
    assert c.esta_pronto()


def test_limpar_curriculo():
    c = Curriculo()
    c.adicionar_dados_pessoais("João", "joao@email.com", "", "")
    c.adicionar_experiencia("Empresa", "Dev", "2023")
    c.limpar()
    assert not c.esta_pronto()
    assert len(c.experiencias) == 0
