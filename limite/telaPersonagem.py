from limite.telaGenerica import TelaGenerica


class TelaPersonagem(TelaGenerica):

    def __init__(self, controlador):
        super(TelaPersonagem, self).__init__(
            controlador=controlador,
            titulo_da_tela="MENU PERSONAGENS",
            opcoes=(
                (1, "Novo jogador"),
                (2, "Listar jogadores"),
                (3, "Excluir jogador"),
                (4, "Novo monstro"),
                (5, "Listar monstros"),
                (6, "Excluir Monstro"),
            )
        )

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

    def pega_dados_do_monstro(self) -> dict:
        return {
            # TODO: implementar
        }

    @staticmethod
    def mostra_jogadores(jogadores: list):
        print("\n------ Lista de jogadores cadastrados ------\n")
        for jogador in jogadores:
            print("{} | {}".format(jogador.codigo, jogador.nome))
    
    @staticmethod
    def mostra_monstros(monstros: list):
        print("\n------ Lista de monstros cadastrados ------\n")
        for monstro in monstros:
            print("{} | {}".format(monstro.codigo, monstro.nome))
