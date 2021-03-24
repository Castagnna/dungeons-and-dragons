from limite.telaGenerica import TelaGenerica


class TelaBackground(TelaGenerica):

    def __init__(self, controlador):
        super(TelaBackground, self).__init__(
            controlador=controlador,
            titulo_da_tela="MENU BACKGROUND",
            opcoes=(
                (1, "Mostrar o mapa"),
            )
        )