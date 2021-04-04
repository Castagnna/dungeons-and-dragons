from controle.controladorGenerico import ControladorGenerico
from limite.telaMonstro import TelaMonstro
from entidade.monstro import Monstro
import pygame


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

    @property
    def monstros(self):
        return self.__monstros

    """
    setters
    """

    """
    methods
    """

    def cria_novo_monstro(self):
        dados = self.__tela.pega_dados_do_jogador()
        if dados['tamanho'] == 'Grande':
            dados['imagem'] = pygame.transform.scale(dados['imagem'], (200, 200))
        elif dados['tamanho'] == 'Enorme':
            dados['imagem'] = pygame.transform.scale(dados['imagem'], (300, 300))
        elif dados['tamanho'] == 'Colossal':
            dados['imagem'] = pygame.transform.scale(dados['imagem'], (400, 400))
        else:
            dados['imagem'] = pygame.transform.scale(dados['imagem'], (100, 100))
        dados['posicao'] = dados['imagem'].get_rect()
        dados['posicao'][0] = 100 * (self.__counta_monstros % 10)
        dados['posicao'][1] = 100 * (self.__counta_monstros // 10)
        novo_monstro = Monstro(
            id=self.__counta_monstros,
            **dados
        )
        self.__counta_monstros += 1
        self.__monstros.append(novo_monstro)
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

    def mapa_moveu(self, x: int, y: int):
        for i in range(len(self.__monstros)):
            posicao = self.__monstros[i].posicao
            self.__monstros[i].posicao(posicao[0] - x, posicao[1] - y)