from limite.telaGenerica import TelaGenerica


class TelaJogador(TelaGenerica):

    def __init__(self, controlador):
        super(TelaJogador, self).__init__(
            controlador=controlador,
            titulo_da_tela="MENU JOGADOR",
            opcoes=(
                (1, "Novo Jogador"),
                (2, "Iniciar combate"),
            )
        )
