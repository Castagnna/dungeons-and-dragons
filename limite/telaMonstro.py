from limite.telaGenerica import TelaGenerica


class TelaMonstro(TelaGenerica):

    def __init__(self, controlador):
        super(TelaMonstro, self).__init__(
            controlador=controlador,
            titulo_da_tela="MENU MONSTRO",
            opcoes=(
                (1, "Novo monstro"),
                (2, "Iniciar combate"),
            )
        )
