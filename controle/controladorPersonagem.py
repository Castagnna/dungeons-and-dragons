from controle.controladorGenerico import ControladorGenerico
from limite.telaPersonagem import TelaPersonagem


class ControladorPersonagem(ControladorGenerico):
    def __init__(self, controlador_principal):
        super(ControladorPersonagem, self).__init__()
        self.__controlador_principal = controlador_principal
        self.__tela = TelaPersonagem(self)
        self.__jogadores = []

    def cria_novo_jogador(self):
        print("Jogador criado")
        return -1

    def iniciar_combate(self):
        print("Batalha")
        return -1

    def mostra_tela(self):

        funcoes = {
            -1: self.mostra_tela,
            0: self.finaliza_programa,
            1: self.cria_novo_jogador,
            2: self.iniciar_combate,
        }

        while True:
            opcao_selecionada = self.__tela.mostra_opcoes()
            funcao_selecionada = funcoes[opcao_selecionada]
            funcao_selecionada()
