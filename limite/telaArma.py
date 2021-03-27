from limite.telaGenerica import TelaGenerica


class TelaArma(TelaGenerica):

    def __init__(self, controlador):
        super(TelaArma, self).__init__(
            controlador=controlador,
            titulo_da_tela="\nMENU ARMA",
            opcoes=(
                (1, "Nova Arma"),
                (2, "Armas cadastradas"),
                (3, "Remove arma")
            )
        )

    def pega_dados_da_arma(self) -> dict:
        nome = self.pega_dado("Nome: ", "str")
        quantidade_dado = self.pega_dado("Quantidade de dados: ", "int")
        numero_faces = self.pega_dado("Numero de faces do dado: ", "int")
        return {
            "nome": nome,
            "quantidade_dado": quantidade_dado,
            "numero_faces": numero_faces,
        }

    def pega_id_arma(self) -> int:
        return self.pega_dado("Id da arma pare remover: ", "int")
        # arma = self.controlador.pega_arma_por_id(id)
        # print("id {} da arma {}".format(id, arma.nome))
        # return id

    @staticmethod
    def mostra_armas(armas: list):
        print("\n------ Lista de armas cadastradas ------")
        for arma in armas:
            print("{} | {}".format(arma.id, arma.nome))
