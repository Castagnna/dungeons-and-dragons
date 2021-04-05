from limite.telaGenerica import TelaGenerica
import pygame

class TelaMonstro(TelaGenerica):

    def __init__(self, controlador):
        super(TelaMonstro, self).__init__(controlador)
        self.__dicio_letras = {'A': 100, 'B': 200, 'C': 300, 'D': 400, 'E': 500,
                               'F': 600, 'G': 700, 'H': 800, 'I': 900, 'J': 1000,
                               'K': 1100, 'L': 1200, 'M': 1300, 'N': 1400, 'O': 1500,
                               'P': 1600, 'Q': 1700, 'R': 1800, 'S': 1900,
                               'T': 2000, 'U': 2100, 'V': 2200, 'W': 2300,
                               'X': 2400, 'Y': 2500, 'Z': 2500}
        self.__dicio_numeros = {'1': 100, '2': 200, '3': 300, '4': 400, '5': 500, '6': 600, '7': 700, '8': 800,
                                '9': 900}

    def mostra_opcoes(self) -> int:
        titulo_da_tela = "MENU MONSTRO"

        opcoes = (
            (1, "Novo monstro"),
            (2, "Listar monstros"),
            (3, "Excluir Monstro"),
            (4, "Cadastrar ataque do monstro"),
            (5, "Excluir ataque do monstro"),
            (6, "Atacar jogador"),
            (7, "Movimentar monstro"),
            (8, "Mostra atributos do monstro"),
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
            "imagem": self.pega_imagem('tokens/'),
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

    def pega_imagem(self, caminho):
        while True:
            try:
                entrada = input('Digite o nome da imagem que pretende usar: ')
                imagem = pygame.image.load(caminho + entrada + '.png')
                return imagem
            except FileNotFoundError:
                print('Imagem não encontrada, favor digitar novamente')
            except:
                print('Erro inesperado, favor entrar em contato com o suporte')

    def mostra_alterar_monstro(self) -> int:
        titulo_da_tela = "ALTERAR MONSTRO"

        opcoes = (
            (1, "Novo nome"),
            (2, "Alterar forca"),
            (3, "Alterar destreza"),
            (4, 'Alterar constituicao'),
            (5, 'Alterar inteligencia'),
            (6, 'Alterar sabedoria'),
            (7, 'Alterar carisma'),
            (8, 'Alterar imagem'),
            (9, 'Alterar ca'),
            (10, 'Alterar vida maxima'),
            (11, 'Alterar tamanho'),
            (12, 'Alterar vida atual'),
            (13, 'Alterar tipo'),
            (14, 'Alterar experiencia')
        )

        self.cria_menu_opcoes(titulo_da_tela, opcoes)

        opcao = self.pega_dado(
            mensagem="\n>>> Escolha uma opção: ",
            tipo="int",
            valores_validos=[codigo for codigo, _ in opcoes],
            confirmar=False
        )

        return opcao

    def movimenta_monstro(self):
        while True:
            try:
                entrada = input('Digite os valores para X (letra) e Y (número): ')
                if len(entrada) != 2 and entrada[0].upper() not in self.__dicio_letras.keys() and entrada[1] not in self.__dicio_numeros.keys():
                    raise AttributeError
                return [self.__dicio_letras[entrada[0].upper()], self.__dicio_numeros[entrada[1]]]
            except AttributeError:
                print('Digite apenas 2 valores, sendo 1 letra X e 1 número para Y')
            except:
                print('Erro inesperado, favor entrar em contato com o suporte')

    def resumo_combate(self, atacante: str, defensor: str, dano: int):
        mensagem = f"{atacante} causou {dano} ao {defensor}"
        self.monstra_mensagem(mensagem)

    @staticmethod
    def mostra_atributos(atributos: dict):
        for atributo, valor in atributos.items():
            print(f"{atributo}: {valor}")

    @staticmethod
    def mostra_ataque_do_monstro(
            id: int,
            nome: str,
            quantidade_dado: int,
            numero_faces: int,
            dano_bonus: int,
            acerto: int,
            cd: int,
            teste: str,
            mostra_titulo: bool = True,
    ):
        if mostra_titulo:
            print("\n----- Ataque do Monstro -----")
        print(f"id: {id}, nome: {nome}, dados: {quantidade_dado}, faces: {numero_faces}, dano bonus: {dano_bonus}, bonus de acerto: {acerto}, cd: {cd}, teste: {teste}")