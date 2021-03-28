from controle.controladorGenerico import ControladorGenerico
from limite.telaPersonagem import TelaPersonagem
from entidade.jogador import Jogador
from entidade.monstro import Monstro


class ControladorPersonagem(ControladorGenerico):
    def __init__(self, controlador_principal):
        super(ControladorPersonagem, self).__init__(TelaPersonagem(self))
        self.__controlador_principal = controlador_principal
        self.__jogadores = []
        self.__counta_personagens = 0
        self.__monstros = []

    @property
    def controlador_principal(self):
        return self.__controlador_principal

    def cria_novo_jogador(self):
        dados = self.tela.pega_dados_do_jogador()
        novo_jogador = Jogador(
            codigo=self.__counta_personagens,
            imagem=None,
            posicao=[0,0],
            **dados
        )
        self.__counta_personagens += 1
        self.__jogadores.append(novo_jogador)
        self.tela.monstra_mensagem("Jogador {} criado com sucesso".format(novo_jogador.nome))

    def mostra_jogadores(self):
        self.tela.mostra_jogadores(self.__jogadores)

    def excluir_jogador(self):
        pass

    def cria_novo_monstro(self):
        pass

    def mostra_monstros(self):
        self.tela.mostra_monstros(self.__monstros)

    def excluir_monstro(self):
        pass

    def atacar(self):
        print("Jogador A ataca B")
        pass

    def lancar_magia(self):
        print("A Lanca Magia em B")
        pass

    def mostra_tela(self):

        funcoes = {
            1: self.cria_novo_jogador,
            2: self.mostra_jogadores,
            3: self.excluir_jogador,
            4: self.cria_novo_monstro,
            5: self.mostra_monstros,
            6: self.excluir_monstro,
            7: self.atacar,
            8: self.lancar_magia,
            88: self.controlador_principal.mostra_tela,
        }

        super(ControladorPersonagem, self).mostra_tela(funcoes)
