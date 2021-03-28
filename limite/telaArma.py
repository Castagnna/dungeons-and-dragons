from limite.telaGenerica import TelaGenerica


class TelaArma(TelaGenerica):

    def __init__(self, controlador):
        super(TelaArma, self).__init__(
            controlador=controlador,
            titulo_da_tela="\nMENU ARMA",
            opcoes=(
                (1, "Nova Arma"),
                (2, "Armas cadastradas"),
                (3, "Remove arma"),
                (4, "Mostra atributos da arma"),
                (5, "Alterar arma"),
                (88, "Voltar")
            )
        )

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
    def mostra_atributos_da_arma(arma):
        print("\n------ Atributos de {} ------".format(arma.nome))
        print("Id: {}".format(arma.id))
        print("Nome: {}".format(arma.nome))
        print("Quantidade dado: {}".format(arma.quantidade_dado))
        print("Numero de faces: {}".format(arma.numero_faces))
