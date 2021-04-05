from limite.telaGenerica import TelaGenerica
import pygame

class TelaBackground(TelaGenerica):

    def __init__(self, controlador):
        super(TelaBackground, self).__init__(controlador)
        self.__dicio_letras = {'A': 100, 'B': 200, 'C': 300, 'D': 400, 'E': 500,
                               'F': 600, 'G': 700, 'H': 800, 'I': 900, 'J': 1000,
                               'K': 1100, 'L': 1200, 'M': 1300, 'N': 1400, 'O': 1500,
                               'P': 1600, 'Q': 1700, 'R': 1800, 'S': 1900,
                               'T': 2000, 'U': 2100, 'V': 2200, 'W': 2300,
                               'X': 2400, 'Y': 2500, 'Z': 2500}
        self.__dicio_numeros = {'1': 100, '2': 200, '3': 300, '4': 400, '5': 500, '6': 600, '7': 700, '8': 800,
                                '9': 900}

    def mostra_opcoes(self):
        titulo_da_tela = "MENU BACKGROUND"

        opcoes = (
            (1, "Criar/Alterar Background"),
            (2, "Movimentar Mapa"),
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

    def movimenta_mapa(self):
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

    def pega_imagem(self, caminho):
        while True:
            try:
                entrada = input('Digite o nome do cenário: ')
                imagem = pygame.image.load(caminho + entrada + '.png')
                return imagem
            except FileNotFoundError:
                print('Imagem não encontrada, favor digitar novamente')
            except:
                print('Erro inesperado, favor entrar em contato com o suporte')

    def erro_movimentacao(self):
        print('Não é possível movimentar algo que não existe, favor inserir um mapa primeiro')