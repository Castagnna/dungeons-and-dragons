from limite.telaGenerica import TelaGenerica


class TelaBackground(TelaGenerica):

    def __init__(self, controlador):
        super(TelaBackground, self).__init__(controlador)

    def mostrar_opcoes(self):
        print('Escolha uma opção')
        print('1 - Criar/Alterar Background')
        print('2 - Movimentar Mapa')
        while True:
            try:
                opcao = int(input('Digite o número correspondente: '))
                if opcao not in [1, 2]:
                    raise ValueError
                return opcao
            except ValueError:
                print('Favor digitar o número correspondete a opção')
            except:
                print('Erro inesperado, favor entrar em contato com o suporte')

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
