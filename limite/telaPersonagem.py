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

    def pega_dados_do_jogador(self) -> dict:
        #nome = self.pega_dado("Nome: ", "str")
        #forca = self.pega_dado("Forca: ", "int")
        #destreza = self.pega_dado("Destreza: ", "int")
        #constituicao = self.pega_dado("Constituicao: ", "int")
        #inteligencia = self.pega_dado("Inteligencia: ", "int")
        #sabedoria = self.pega_dado("Sabedoria: ", "int")
        #carisma = self.pega_dado("Carisma: ", "int")
        #imagem: pygame.image.load,
        #ca = self.pega_dado("Ca: ", "int")
        #vida_maxima = self.pega_dado("Vida maxima: ", "int")
        #vida_atual = self.pega_dado("Vida atual: ", "int")
        #tamanho = self.pega_dado("Tamanho: ", "str")
        #posicao: list,
        #nome_jogador = self.pega_dado("Nome do jogador: ", "str")
        #level = self.pega_dado("Level: ", "int")
        #experiencia = self.pega_dado("Experiencia: ", "int")
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
