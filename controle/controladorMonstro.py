from controle.controladorGenerico import ControladorGenerico
from limite.telaMonstro import TelaMonstro
from entidade.monstro import Monstro


class ControladorMonstro(ControladorGenerico):
    def __init__(self, controlador_principal):
        super(ControladorMonstro, self).__init__(TelaMonstro(self))
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

    def cria_novo_monstro(self):
        dados = self.tela.pega_dados_do_monstro()
        novo_monstro = Monstro(
            id=self.__counta_monstros,
            posicao=[0, 0],
            imagem=None,
            **dados
        )
        self.__monstros.append(novo_monstro)
        self.__counta_monstros += 1
        self.tela.executado_com_sucesso()

    def pega_monstro_por_id(self):
        if self.__monstros:
            valores_validos = [monstro.id for monstro in self.__monstros]
            id = self.tela.pega_id(valores_validos)
            for monstro in self.__monstros:
                if monstro.id == id:
                    return monstro
        else:
            self.tela.lista_monstros_vazia()
            return None

    def mostra_monstros(self):
        self.tela.mostra_monstros(self.__monstros)

    def excluir_monstro(self):
        monstro = self.pega_monstro_por_id()
        try:
            remover = self.tela.confirma_remocao(monstro.nome)
        except AttributeError:
            pass
        else:
            if remover:
                self.__monstros.remove(monstro)
                self.tela.executado_com_sucesso()

    def atacar(self):
        print("monstro A ataca B")
        pass

    def lancar_magia(self):
        print("A Lanca Magia em B")
        pass

    def mostra_tela(self):

        funcoes = {
            1: self.cria_novo_monstro,
            2: self.mostra_monstros,
            3: self.excluir_monstro,
            7: self.atacar,
            8: self.lancar_magia,
        }

        super(ControladorMonstro, self).mostra_tela(funcoes)
