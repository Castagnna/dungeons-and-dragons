from controle.controladorGenerico import ControladorGenerico
from limite.telaMagia import TelaMagia
from entidade.magia import Magia


class ControladorMagia(ControladorGenerico):
    def __init__(self, controlador_jogador):
        super(ControladorMagia, self).__init__(TelaMagia(self))
        self.__controlador_jogador = controlador_jogador
        self.__counta_magias = 0,

    def cria_magia(self, jogador):
        dados = self.tela.pega_dados_da_magia()
        magia = Magia(
            id=self.__counta_magias,
            **dados
        )
        jogador.append(magia)
        self.__counta_magias += 1
        self.tela.monstra_mensagem("Magia {} criada com sucesso".format(magia.nome))

    def mostra_tela(self):

        funcoes = {
            (1, self.cria_magia),
        }

        super(ControladorMagia, self).mostra_tela(funcoes)
