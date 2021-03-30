from limite.telaGenerica import TelaGenerica


class TelaPrincipal(TelaGenerica):

    def __init__(self, controlador):
        super(TelaPrincipal, self).__init__(controlador)

    def mostra_opcoes(self) -> int:
        titulo_da_tela = "MENU PRINCIPAL"

        opcoes = (
            (1, "Menu Jogador"),
            (2, "Menu Monstro"),
            (3, "Menu Arma"),
            (99, "Finaliza programa")
        )

        self.cria_menu_opcoes(titulo_da_tela, opcoes)

        opcao = self.pega_dado(
            mensagem="\n>>> Escolha uma opção: ",
            tipo="int",
            valores_validos=[codigo for codigo, _ in opcoes],
            confirmar=False
        )

        return self.protege_finalizar(opcao)
