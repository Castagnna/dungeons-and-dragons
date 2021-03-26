from limite.telaGenerica import TelaGenerica
from controle.controladorMagia import ControladorMagia

class TelaMagia(TelaGenerica):

    def __init__(self, controlador):
        super(TelaMagia, self).__init__(
            controlador=controlador,
            titulo_da_tela="MENU MAGIA",
            opcoes=(
                (1, "Nova magia"),
                (2, "Apaga magia"),
            )
        )
