from limite.telaGenerica import TelaGenerica


class TelaPrincipal(TelaGenerica):

    def __init__(self, controlador):
        super(TelaPrincipal, self).__init__(
            controlador=controlador,
            titulo_da_tela="MENU PRINCIPAL",
            opcoes=(
                (1, "Cadastra Jogador"),
                (2, "Cadastra Monstro"),
            )
        )
