from limite.telaGenerica import TelaGenerica
from pygame.image import load


class TelaMonstro(TelaGenerica):

    def __init__(self, controlador):
        super(TelaMonstro, self).__init__(controlador)

    def mostra_opcoes(self) -> int:
        titulo_da_tela = "MENU MONSTRO"

        opcoes = (
            (1, "Novo monstro"),
            (2, "Listar monstros"),
            (3, "Excluir Monstro"),
            (4, "Mostra atributos do monstro"),
            (9, "Atacar jogador"),
            (77, "Cria monstro teste"),
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

    def pega_dados_do_monstro(self) -> dict:
        valores_validos = [
            "Minusculo",
            "Pequeno",
            "Medio",
            "Grande",
            "Enorme",
            "Colossal"
        ]

        return {
            "nome": self.pega_dado("Nome: ", "str"),
            "forca": self.pega_dado("Forca: ", "int"),
            "destreza": self.pega_dado("Destreza: ", "int"),
            "constituicao": self.pega_dado("Constituicao: ", "int"),
            "inteligencia": self.pega_dado("Inteligencia: ", "int"),
            "sabedoria": self.pega_dado("Sabedoria: ", "int"),
            "carisma": self.pega_dado("Carisma: ", "int"),
            "imagem": self.pega_imagem(),
            "ca": self.pega_dado("Ca: ", "int"),
            "vida_maxima": self.pega_dado("Vida maxima: ", "int"),
            "vida_atual": self.pega_dado("Vida atual: ", "int"),
            "tamanho": self.pega_dado("Tamanho: ", "str", valores_validos),
            "tipo": self.pega_dado("Tipo: ", "str"),
            "experiencia": self.pega_dado("Experiencia: ", "int"),
        }
    
    @staticmethod
    def mostra_monstros(monstros: list):
        print("\n------ Lista de monstros cadastrados ------\n")
        for monstro in monstros:
            print(f"{monstro.id} | {monstro.nome}")

    def lista_monstros_vazia(self):
        self.monstra_mensagem("A lista de monstros esta vazia")

    def confirma_remocao(self, nome: str):
        return self.tela_confirma("Remover >> {} << ?".format(nome))

    def monstro_removido_com_sucesso(self, nome: str):
        self.monstra_mensagem("Monstro {} excluido com sucesso".format(nome))

    def pega_dano(self):
        return self.pega_dado("Insira o valor de dano: ", "int", None, True)

    @staticmethod
    def resumo_combate(atacante: str, defensor: str, dano: int):
        print(f"{atacante} causou {dano} ao {defensor}")

    def pega_id_monstro(self, valores_validos) -> int:
        print("Monstro, ", end="")
        return self.pega_id(valores_validos)

    @staticmethod
    def pega_imagem():
        tentativas = 0
        while tentativas < 2:
            try:
                nome = input("Nome do arquivo de imagem: ")
                imagem = load("imagens/" + nome + ".png")
                return imagem
            except FileNotFoundError:
                print(f"Imagem não encontrada, favor digitar novamente ({tentativas})")
                tentativas += 1
        print("Numero de tantativa esgotado, iniciado com imagem padrao")
        return load("imagens/monstro.png")

    def resumo_combate(self, atacante: str, defensor: str, dano: int):
        mensagem = f"{atacante} causou {dano} ao {defensor}"
        self.monstra_mensagem(mensagem)

    @staticmethod
    def mostra_atributos(atributos: dict):
        for atributo, valor in atributos.items():
            print(f"{atributo}: {valor}")
