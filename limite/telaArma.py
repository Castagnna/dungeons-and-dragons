from limite.telaGenerica import TelaGenerica


class TelaArma(TelaGenerica):

    def __init__(self, controlador):
        super(TelaArma, self).__init__(controlador)

    def mostra_opcoes(self) -> int:
        titulo_da_tela = "MENU ARMA"

        opcoes = (
            (1, "Nova arma"),
            (2, "Armas cadastradas"),
            (3, "Remove arma"),
            (4, "Mostra atributos da arma"),
            (5, "Alterar arma"),
            (77, "Cria arma teste"),
            (88, "Voltar"),
            (99, "Finaliza programa")
        )

        self.cria_menu_opcoes(titulo_da_tela, opcoes)

        opcao = self.pega_dado(
            mensagem="\n>>> Escolha uma opção: ",
            tipo="int",
            valores_validos=[codigo for codigo, _ in opcoes],
            confirmar=False
        )

        return self.protege_finalizar(opcao)

    def pega_dados_da_arma(self) -> dict:
        return {
            "nome": self.pega_dado("Nome: ", "str"),
            "quantidade_dado": self.pega_dado("Quantidade de dados: ", "int"),
            "numero_faces": self.pega_dado("Numero de faces do dado: ", "int"),
        }

    @staticmethod
    def mostra_armas(armas: list):
        print("\n------ Lista de armas cadastradas ------")
        for arma in armas:
            print("{} | {}".format(arma.id, arma.nome))

    @staticmethod
    def mostra_atributos_da_arma(atributos):
        print("\n------ Atributos da arma ------")
        print(f"Id: {atributos['id']}")
        print(f"Nome: {atributos['nome']}")
        print(f"Quantidade dado: {atributos['dados']}")
        print(f"Numero de faces: {atributos['faces']}")

    def mostra_alterar_arma(self) -> int:
        titulo_da_tela = "ALTERAR ARMA"

        opcoes = (
            (1, "Novo nome"),
            (2, "Alterar quantidade de dados"),
            (3, "Alterar faces"),
        )

        self.cria_menu_opcoes(titulo_da_tela, opcoes)

        opcao = self.pega_dado(
            mensagem="\n>>> Escolha uma opção: ",
            tipo="int",
            valores_validos=[codigo for codigo, _ in opcoes],
            confirmar=False
        )

        return opcao

    def lista_armas_vazia(self):
        self.monstra_mensagem("A lista de armas esta vazia")

    def confirma_remocao(self, nome: str):
        return self.tela_confirma("Remover >> {} << ?".format(nome))

    def arma_removida_com_sucesso(self, nome: str):
        self.monstra_mensagem("Arma {} excluida com sucesso".format(nome))