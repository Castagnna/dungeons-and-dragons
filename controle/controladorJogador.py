from controle.controladorGenerico import ControladorGenerico
from controle.controladorArma import ControladorArma
from limite.telaJogador import TelaJogador
from entidade.jogador import Jogador


class ControladorJogador(ControladorGenerico):
    def __init__(self, controlador_principal):
        super(ControladorJogador, self).__init__(TelaJogador(self))
        self.__controlador_principal = controlador_principal
        # try:
        #     self.__controlador_arma = controlador_principal.controlador_arma
        # except AttributeError:
        #     controlador_principal.controlador_arma = ControladorArma(controlador_principal)
        self.__controlador_arma = controlador_principal.controlador_arma
        self.__jogadores = []
        self.__counta_jogadores = 0

    """
    getters
    """

    @property
    def controlador_principal(self):
        return self.__controlador_principal

    @property
    def jogadores(self) -> list:
        return self.__jogadores

    @property
    def controlador_arma(self):
        return self.__controlador_arma

    """
    methods
    """

    def cria_novo_jogador(self):
        dados = self.tela.pega_dados_do_jogador()
        novo_jogador = Jogador(
            codigo=self.__counta_jogadores,
            imagem=None,
            posicao=[0, 0],
            **dados
        )
        self.__jogadores.append(novo_jogador)
        self.__counta_jogadores += 1
        self.tela.monstra_mensagem("Jogador {} criado com sucesso".format(novo_jogador.nome))

    def mostra_jogadores(self):
        self.tela.mostra_jogadores(self.__jogadores)

    def pega_jogador_por_id(self):
        if self.__jogadores:
            valores_validos = [jogador.codigo for jogador in self.__jogadores]
            codigo = self.tela.pega_dado("Id do jogador: ", "int", valores_validos, False)
            for jogador in self.__jogadores:
                if jogador.codigo == codigo:
                    return jogador
        else:
            self.tela.lista_jogadores_vazia()
            return None

    def remove_jogador(self):
        jogador = self.pega_jogador_por_id()
        try:
            remover = self.tela.confirma_remocao(jogador.nome)
        except AttributeError:
            pass
        else:
            if remover:
                self.__jogadores.remove(jogador)
                self.tela.jogador_removido_com_sucesso(jogador.nome)

    def equipar_arma(self):
        self.mostra_jogadores()
        jogador = self.pega_jogador_por_id()
        if not jogador:
            return
        self.__controlador_arma.mostra_armas()
        arma = self.__controlador_arma.pega_arma_por_id()
        if not arma:
            return
        jogador.adiciona_arma(arma)

    def mostrar_armas_do_jogador(self):
        jogador = self.pega_jogador_por_id()
        if not jogador:
            return
        atributos_armas = [
            (
                arma.id, arma.nome, arma.quantidade_dado, arma.numero_faces
            )
            for arma in jogador.armas if jogador.armas
        ]
        self.tela.mostra_armas_do_jogador(atributos_armas)

    def lancar_magia(self):
        print("A Lanca Magia em B")
        pass

    def mostra_tela(self):

        funcoes = {
            1: self.cria_novo_jogador,
            2: self.mostra_jogadores,
            3: self.remove_jogador,
            4: self.equipar_arma,
            5: self.mostrar_armas_do_jogador,
            8: self.lancar_magia,
            88: self.controlador_principal.mostra_tela,
        }

        super(ControladorJogador, self).mostra_tela(funcoes)
