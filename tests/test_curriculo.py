import json
import os
import sys
from unittest.mock import MagicMock, patch

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from curriculo import Curriculo
from viacep import buscar_cidade_por_cep


# ── Testes da classe Curriculo ────────────────────────────────────────────────

def test_adicionar_dados_pessoais():
    c = Curriculo()

    c.adicionar_dados_pessoais(
        "Geovanna",
        "geo@email.com",
        "61999999999",
        "Brasilia - DF",
    )

    assert c.dados_pessoais["nome"] == "Geovanna"
    assert c.dados_pessoais["email"] == "geo@email.com"


def test_nome_vazio():
    c = Curriculo()

    with pytest.raises(ValueError):
        c.adicionar_dados_pessoais(
            "",
            "teste@email.com",
            "61999999999",
            "Brasilia - DF",
        )


def test_email_invalido():
    c = Curriculo()

    with pytest.raises(ValueError):
        c.adicionar_dados_pessoais(
            "Geovanna",
            "emailinvalido",
            "61999999999",
            "Brasilia - DF",
        )


def test_adicionar_experiencia():
    c = Curriculo()

    c.adicionar_experiencia(
        "Google",
        "Desenvolvedor",
        "2022-2024",
    )

    assert len(c.experiencias) == 1
    assert c.experiencias[0]["empresa"] == "Google"


def test_remover_experiencia():
    c = Curriculo()

    c.adicionar_experiencia(
        "Google",
        "Dev",
        "2022",
    )

    c.remover_experiencia(0)

    assert len(c.experiencias) == 0


def test_adicionar_formacao():
    c = Curriculo()

    c.adicionar_formacao(
        "CEUB",
        "ADS",
        "2026",
    )

    assert len(c.formacoes) == 1
    assert c.formacoes[0]["curso"] == "ADS"


def test_remover_formacao():
    c = Curriculo()

    c.adicionar_formacao(
        "CEUB",
        "ADS",
        "2026",
    )

    c.remover_formacao(0)

    assert len(c.formacoes) == 0


def test_curriculo_pronto():
    c = Curriculo()

    c.adicionar_dados_pessoais(
        "Geovanna",
        "geo@email.com",
        "61999999999",
        "Brasilia - DF",
    )

    assert c.esta_pronto() is True


def test_curriculo_nao_pronto():
    c = Curriculo()

    assert c.esta_pronto() is False


# ── Testes da API ViaCEP ──────────────────────────────────────────────────────

def test_buscar_cidade_por_cep_sucesso():
    resposta_mock = {
        "localidade": "Brasilia",
        "uf": "DF",
    }

    mock_response = MagicMock()
    mock_response.read.return_value = json.dumps(resposta_mock).encode("utf-8")
    mock_response.__enter__.return_value = mock_response

    with patch("urllib.request.urlopen", return_value=mock_response):
        resultado = buscar_cidade_por_cep("70040010")

    assert resultado == "Brasilia - DF"


def test_buscar_cidade_por_cep_invalido():
    resposta_mock = {
        "erro": True,
    }

    mock_response = MagicMock()
    mock_response.read.return_value = json.dumps(resposta_mock).encode("utf-8")
    mock_response.__enter__.return_value = mock_response

    with patch("urllib.request.urlopen", return_value=mock_response):
        with pytest.raises(ValueError, match="CEP nao encontrado"):
            buscar_cidade_por_cep("00000000")