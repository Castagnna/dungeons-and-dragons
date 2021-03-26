from limite.telaGenerica import TelaGenerica
from controle.controladorArma import ControladorArma


class TelaArma(TelaGenerica):

    def __init__(self, controlador):
        super(TelaArma, self).__init__(
            controlador=controlador,
            titulo_da_tela="MENU Arma",
            opcoes=(
                (1, "Nova Arma"),
                (2, "Armas cadastradas"),
            )
        )

    def pega_dados_da_arma(self) -> dict:
        nome = self.pega_dado("Nome: ", "str")
        dano = self.pega_dado("Dano: ", "str")
        return {
            "nome": nome,
            "dano": dano,
        }

    @staticmethod
    def mostra_armas(armas: list):
        print("Armas cadastradas: {}".format(armas))
