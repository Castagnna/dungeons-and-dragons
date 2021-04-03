from controle.controladorGenerico import ControladorGenerico
from controle.controladorMonstro import ControladorMonstro
from controle.controladorMagia import ControladorMagia
from limite.telaJogador import TelaJogador
from entidade.jogador import Jogador


class ControladorJogador(ControladorGenerico):
    def __init__(self, controlador_principal):
        super(ControladorJogador, self).__init__(TelaJogador(self))
        self.__controlador_principal = controlador_principal
        self.__controlador_arma = controlador_principal.controlador_arma
        self.__controlador_monstro = None
        self.__controlador_magia = ControladorMagia(self)
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

    @property
    def controlador_monstro(self):
        return self.__controlador_monstro

    """
    setters
    """

    @controlador_monstro.setter
    def controlador_monstro(self, controlador: ControladorMonstro):
        if isinstance(controlador, ControladorMonstro):
            self.__controlador_monstro = controlador

    """
    methods
    """

    def add_controlador_monstro(self, controlador_monstro: ControladorMonstro):
        if controlador_monstro and isinstance(controlador_monstro, ControladorMonstro):
            if controlador_monstro != self.__controlador_monstro:
                self.__controlador_monstro = controlador_monstro
            if self != controlador_monstro.controlador_jogador:
                controlador_monstro.controlador_jogador = self

    def cria_novo_jogador(self):
        dados = self.tela.pega_dados_do_jogador()
        novo_jogador = Jogador(
            id=self.__counta_jogadores,
            imagem=None,
            posicao=[0, 0],
            **dados
        )
        self.__jogadores.append(novo_jogador)
        self.__counta_jogadores += 1
        self.tela.executado_com_sucesso()

    def mostra_jogadores(self):
        self.tela.mostra_jogadores(self.__jogadores)

    def pega_jogador_por_id(self):
        if self.__jogadores:
            valores_validos = [jogador.id for jogador in self.__jogadores]
            id = self.tela.pega_id(valores_validos)
            for jogador in self.__jogadores:
                if jogador.id == id:
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
                self.tela.executado_com_sucesso()

    def mostra_atributos_do_jogador(self):
        pass

    def altera_atributos_do_jogador(self):
        pass

    def equipar_arma(self):
        self.mostra_jogadores()
        jogador = self.pega_jogador_por_id()
        if not jogador:
            return
        self.__controlador_arma.mostra_armas()
        arma = self.__controlador_arma.pega_arma_por_id()
        if not arma:
            return
        if not (arma in jogador.armas):
            jogador.adiciona_arma(arma)
            self.tela.executado_com_sucesso()

    def mostrar_armas_do_jogador(self, jogador: Jogador = None):

        if not jogador:
            jogador = self.pega_jogador_por_id()

        if jogador and jogador.armas:
            mostra_titulo = True
            for arma in jogador.armas:
                atributos_arma = {
                    "id": arma.id,
                    "nome": arma.nome,
                    "quantidade_dado": arma.quantidade_dado,
                    "numero_faces": arma.numero_faces
                }
                self.tela.mostra_arma_do_jogador(**atributos_arma, mostra_titulo=mostra_titulo)
                mostra_titulo = False

    def pega_arma_do_jogador_por_id(self, jogador: Jogador):
        self.mostrar_armas_do_jogador(jogador)
        if jogador.armas:
            id_para_arma = {arma.id: arma for arma in jogador.armas}
            id = self.tela.pega_id(id_para_arma.keys())
            return id_para_arma[id]
        else:
            return None

    def desequipar_arma(self):
        self.mostra_jogadores()
        jogador = self.pega_jogador_por_id()
        if not jogador:
            return
        arma = self.pega_arma_do_jogador_por_id(jogador)
        if arma:
            jogador.armas.remove(arma)
            self.tela.executado_com_sucesso()

    def atacar(self):
        atacante = self.pega_jogador_por_id()
        if not atacante:
            return
        defensor = self.controlador_monstro.pega_monstro_por_id()
        if not defensor:
            return

        print(f"Atacante {atacante}, defensor {defensor}")

    def lancar_magia(self):
        print("Jogador A Lanca Magia em B")
        pass

    def mostra_tela(self):

        funcoes = {
            1: self.cria_novo_jogador,
            2: self.mostra_jogadores,
            3: self.remove_jogador,
            4: self.mostra_atributos_do_jogador,
            5: self.altera_atributos_do_jogador,
            6: self.equipar_arma,
            7: self.desequipar_arma,
            8: self.mostrar_armas_do_jogador,
            9: self.atacar,
            10: self.lancar_magia,
        }

        super(ControladorJogador, self).mostra_tela(funcoes)
