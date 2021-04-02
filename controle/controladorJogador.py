from controle.controladorGenerico import ControladorGenerico
from limite.telaJogador import TelaJogador
from entidade.jogador import Jogador


class ControladorJogador(ControladorGenerico):
    def __init__(self, controlador_principal):
        super(ControladorJogador, self).__init__(TelaJogador(self))
        self.__controlador_principal = controlador_principal
        self.__controlador_arma = controlador_principal.controlador_arma
        self.__jogadores = []
        self.__counta_jogadores = 0

    @property
    def controlador_principal(self):
        return self.__controlador_principal

    def cria_novo_jogador(self):
        dados = self.tela.pega_dados_do_jogador()
        novo_jogador = Jogador(
            codigo=self.__counta_jogadores,
            imagem=None,
            posicao=[0,0],
            **dados
        )
        self.__counta_jogadores += 1
        self.__jogadores.append(novo_jogador)
        self.tela.monstra_mensagem("Jogador {} criado com sucesso".format(novo_jogador.nome))

    def mostra_jogadores(self):
        self.tela.mostra_jogadores(self.__jogadores)

    def excluir_jogador(self):
        pass

    def equipar_arma(self):
        pass

    def lancar_magia(self):
        print("A Lanca Magia em B")
        pass

    def mostra_tela(self):

        funcoes = {
            1: self.cria_novo_jogador,
            2: self.mostra_jogadores,
            3: self.excluir_jogador,
            7: self.equipar_arma,
            8: self.lancar_magia,
            88: self.controlador_principal.mostra_tela,
        }

        super(ControladorJogador, self).mostra_tela(funcoes)
