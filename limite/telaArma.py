from limite.telaGenerica import TelaGenerica


class TelaArma(TelaGenerica):

    def __init__(self, controlador):
        super(TelaArma, self).__init__(
            controlador=controlador,
            titulo_da_tela="MENU Arma",
            opcoes=(
                (1, "Nova Arma"),
                (2, "Apaga Arma"),
            )
        )
