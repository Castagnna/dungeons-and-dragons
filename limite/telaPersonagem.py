from limite.telaGenerica import TelaGenerica


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
