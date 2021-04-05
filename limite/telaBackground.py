from limite.telaGenerica import TelaGenerica


class TelaBackground(TelaGenerica):

    def __init__(self, controlador):
        super(TelaBackground, self).__init__(controlador)

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
                entrada = [int(w) for w in input('Digite os valores para X e Y separados por espaço: ').split()]
                if len(entrada) != 2:
                    raise AttributeError
                return entrada
            except ValueError:
                print('Digite apenas números para os valores de X e Y')
            except AttributeError:
                print('Digite apenas 2 valores, sendo 1 para X e outro para Y, separados por espaço')
            except:
                print('Erro inesperado, favor entrar em contato com o suporte')

    def pede_imagem(self, caminho):
        return super(TelaBackground, self).pega_imagem(caminho)