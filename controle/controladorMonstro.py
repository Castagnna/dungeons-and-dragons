from controle.controladorGenerico import ControladorGenerico
from limite.telaJogador import TelaJogador
from entidade.monstro import Monstro


# TODO: ajustar para monstro
class ControladorMonstro(ControladorGenerico):
    def __init__(self, controlador_principal):
        super(ControladorMonstro, self).__init__(TelaJogador(self))
        self.__controlador_principal = controlador_principal
        self.__controlador_ataque_monstro = controlador_principal.controlador_ataque_monstro
        self.__controlador_jogador = controlador_principal.controlador_jogador
        self.__monstros = []
        self.__counta_monstros = 0

    """
    getters
    """

    @property
    def controlador_principal(self):
        return self.__controlador_principal

    @property
    def controlador_ataque_monstro(self):
        return self.__controlador_ataque_monstro

    @property
    def controlador_jogador(self):
        return self.__controlador_jogador

    """
    setters
    """

    """
    methods
    """

    def cria_novo_jogador(self):
        dados = self.tela.pega_dados_do_jogador()
        novo_monstro = Monstro(
            id=self.__counta_monstros,
            posicao=[0, 0],
            **dados
        )
        self.__monstros.append(novo_monstro)
        self.__counta_monstros += 1
        self.tela.monstra_mensagem("Monstro {} criado com sucesso".format(novo_monstro.nome))

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
            2: self.mostra_monstros,
            3: self.excluir_monstro,
            7: self.atacar,
            8: self.lancar_magia,
        }

        super(ControladorMonstro, self).mostra_tela(funcoes)
