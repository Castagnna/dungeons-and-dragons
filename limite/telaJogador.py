from limite.telaGenerica import TelaGenerica


class TelaJogador(TelaGenerica):

    def __init__(self, controlador):
        super(TelaJogador, self).__init__(controlador)

    def mostra_opcoes(self) -> int:
        titulo_da_tela = "MENU JOGADOR"

        opcoes = (
            (1, "Novo jogador"),
            (2, "Listar jogadores"),
            (3, "Excluir jogador"),
            (88, "Voltar"),
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

    def pega_dados_do_jogador(self) -> dict:
        return {
            "nome": self.pega_dado("Nome: ", "str"),
            "forca": self.pega_dado("Forca: ", "int"),
            "destreza": self.pega_dado("Destreza: ", "int"),
            "constituicao": self.pega_dado("Constituicao: ", "int"),
            "inteligencia": self.pega_dado("Inteligencia: ", "int"),
            "sabedoria": self.pega_dado("Sabedoria: ", "int"),
            "carisma": self.pega_dado("Carisma: ", "int"),
            "ca": self.pega_dado("Ca: ", "int"),
            "vida_maxima": self.pega_dado("Vida maxima: ", "int"),
            "vida_atual": self.pega_dado("Vida atual: ", "int"),
            "tamanho": self.pega_dado("Tamanho: ", "str"),
            "nome_jogador": self.pega_dado("Nome do jogador: ", "str"),
            "level": self.pega_dado("Level: ", "int"),
            "experiencia": self.pega_dado("Experiencia: ", "int"),
        }

    @staticmethod
    def mostra_jogadores(jogadores: list):
        print("\n------ Lista de jogadores cadastrados ------\n")
        for jogador in jogadores:
            print("{} | {}".format(jogador.codigo, jogador.nome))
