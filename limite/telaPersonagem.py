from limite.telaGenerica import TelaGenerica
from controle.controladorPersonagem import ControladorPersonagem

class TelaPersonagem(TelaGenerica):

    def __init__(self, controlador):
        super(TelaPersonagem, self).__init__(
            controlador=controlador,
            titulo_da_tela="MENU PERSONAGENS",
            opcoes=(
                (1, "Novo jogador"),
                (2, "Novo monstro"),
            )
        )

    def pega_dados_do_jogador(self) -> dict:
        nome = self.pega_dado("Nome: ", "str")
        level = self.pega_dado("Idade: ", "int")
        return {
            "nome": nome,
            "level": level,
        }
