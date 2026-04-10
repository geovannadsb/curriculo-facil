# 📄 CurrículoFácil

![CI](https://github.com/Sgeovannadsb/curriculo-facil/actions/workflows/ci.yml/badge.svg)

> Versão: **1.0.0**

---

## 🎯 Problema Real

Muitas pessoas, especialmente jovens em busca do primeiro emprego, têm dificuldade em criar um currículo profissional bem estruturado. A falta de ferramentas simples e acessíveis faz com que oportunidades sejam perdidas por causa de documentos mal formatados ou incompletos.

## 💡 Solução

**CurrículoFácil** é uma aplicação desktop com interface gráfica (GUI) que guia o usuário no preenchimento de seus dados pessoais, experiências profissionais e formação acadêmica, gerando automaticamente um arquivo PDF formatado e profissional.

## 👥 Público-alvo

- Jovens em busca do primeiro emprego
- Pessoas sem familiaridade com editores de texto
- Qualquer pessoa que queira gerar um currículo rápido e organizado

---

## ✨ Funcionalidades

- Cadastro de dados pessoais (nome, e-mail, telefone, cidade)
- Adição e remoção de experiências profissionais
- Adição e remoção de formações acadêmicas
- Geração de PDF formatado com um clique
- Interface gráfica intuitiva com abas organizadas
- Validação de campos obrigatórios

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Uso |
|------------|-----|
| Python 3.10+ | Linguagem principal |
| Tkinter | Interface gráfica (GUI) |
| fpdf2 | Geração do PDF |
| pytest | Testes automatizados |
| ruff | Linting / análise estática |
| GitHub Actions | CI — Integração Contínua |

---

## 📦 Instalação

### Pré-requisitos

- Python 3.10 ou superior instalado
- pip

### Passos

```bash
# 1. Clone o repositório
git clone https://github.com/geovannadsb/curriculo-facil.git
cd curriculo-facil

# 2. (Opcional) Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# 3. Instale as dependências
pip install -r requirements.txt
```

---

## ▶️ Como Executar

```bash
python src/app.py
```

A janela do aplicativo abrirá. Navegue pelas abas, preencha os dados e clique em **"Gerar PDF do Currículo"**.

---

## 🧪 Como Rodar os Testes

```bash
pytest tests/ -v
```

Os testes cobrem: dados pessoais válidos e inválidos, experiências, formações, remoção de itens, estado do currículo e limpeza de dados.

---

## 🔍 Como Rodar o Lint

```bash
ruff check src/
```

Para corrigir automaticamente problemas simples:

```bash
ruff check src/ --fix
```

---

## 📁 Estrutura do Projeto

```
curriculo-facil/
├── src/
│   ├── app.py           # Interface gráfica (Tkinter)
│   ├── curriculo.py     # Lógica de negócio
│   └── gerador_pdf.py   # Geração do PDF
├── tests/
│   └── test_curriculo.py
├── .github/
│   └── workflows/
│       └── ci.yml       # Pipeline de CI
├── README.md
├── .gitignore
├── pyproject.toml       # Versão e config do ruff
└── requirements.txt
```

---

## 👤 Autor

**Geovanna dos Santos Benedito**  
Bootcamp II — Campus Virtual 2026/1  
🔗 [github.com/geovannadsb/curriculo-facil](https://github.com/geovannadsb/curriculo-facil)
