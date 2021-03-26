from limite.telaGenerica import TelaGenerica
from controle.controladorataquemonstro import ControladorAtaqueMonstro


class TelaAtaqueMonstro(TelaGenerica):

    def __init__(self, controlador):
        super(TelaAtaqueMonstro, self).__init__(
            controlador=controlador,
            titulo_da_tela="MENU ATAQUE MONSTRO",
            opcoes=(
                (1, "Nova ataque"),
                (2, "Apaga ataque"),
            )
        )
