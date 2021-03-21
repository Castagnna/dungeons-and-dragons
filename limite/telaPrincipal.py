from limite.telaGenerica import TelaGenerica


class TelaPrincipal(TelaGenerica):

    def __init__(self, controlador):
        super(TelaPrincipal, self).__init__(
            controlador=controlador,
            titulo_da_tela="MENU PRINCIPAL",
            id_opcoes=(1, 2),
            opcoes=(
                "Cadastra Jogador",
                "Cadastra Monstro",
            )
        )
