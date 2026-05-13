import urllib.request
import json


def buscar_cidade_por_cep(cep):
    cep = cep.replace("-", "").strip()
    if len(cep) != 8 or not cep.isdigit():
        raise ValueError("CEP invalido. Digite 8 numeros.")
    url = f"https://viacep.com.br/ws/{cep}/json/"
    with urllib.request.urlopen(url, timeout=5) as response:
        dados = json.loads(response.read().decode())
    if "erro" in dados:
        raise ValueError("CEP nao encontrado.")
    cidade = dados.get("localidade", "")
    estado = dados.get("uf", "")
    return f"{cidade} - {estado}"
