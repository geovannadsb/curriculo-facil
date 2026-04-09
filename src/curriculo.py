class Curriculo:
    def __init__(self):
        self.dados_pessoais = {}
        self.experiencias = []
        self.formacoes = []

    def adicionar_dados_pessoais(self, nome, email, telefone, cidade):
        if not nome or not email:
            raise ValueError("Nome e e-mail são obrigatórios.")
        self.dados_pessoais = {
            "nome": nome,
            "email": email,
            "telefone": telefone,
            "cidade": cidade,
        }

    def adicionar_experiencia(self, empresa, cargo, periodo):
        if not empresa or not cargo:
            raise ValueError("Empresa e cargo são obrigatórios.")
        self.experiencias.append(
            {"empresa": empresa, "cargo": cargo, "periodo": periodo}
        )

    def remover_experiencia(self, indice):
        if indice < 0 or indice >= len(self.experiencias):
            raise IndexError("Índice de experiência inválido.")
        self.experiencias.pop(indice)

    def adicionar_formacao(self, instituicao, curso, ano):
        if not instituicao or not curso:
            raise ValueError("Instituição e curso são obrigatórios.")
        self.formacoes.append(
            {"instituicao": instituicao, "curso": curso, "ano": ano}
        )

    def remover_formacao(self, indice):
        if indice < 0 or indice >= len(self.formacoes):
            raise IndexError("Índice de formação inválido.")
        self.formacoes.pop(indice)

    def esta_pronto(self):
        return bool(self.dados_pessoais)

    def limpar(self):
        self.dados_pessoais = {}
        self.experiencias = []
        self.formacoes = []
