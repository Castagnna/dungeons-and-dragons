from limite.telaGenerica import TelaGenerica
from controle.controladorPrincipal import ControladorPrincipal

class TelaPrincipal(TelaGenerica):

    def __init__(self, controlador):
        super(TelaPrincipal, self).__init__(
            controlador=controlador,
            titulo_da_tela="MENU PRINCIPAL",
            opcoes=(
                (1, "Menu Personagem"),
                (2, "Menu Arma"),
            )
        )
