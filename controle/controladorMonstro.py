from controle.controladorGenerico import ControladorGenerico
from limite.telaMonstro import TelaMonstro
from entidade.monstro import Monstro
import pygame


class ControladorMonstro(ControladorGenerico):
    def __init__(self, controlador_principal):
        super(ControladorMonstro, self).__init__(TelaMonstro(self))
        self.__controlador_principal = controlador_principal
        self.__controlador_relatorio = controlador_principal.controlador_relatorio
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

    def cria_novo_monstro(self, dados: dict = None):
        if not dados:
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

    def cria_monstro_teste(self):
        dados = {
            "nome": f"dragao {self.__counta_monstros}",
            "forca": 1,
            "destreza": 1,
            "constituicao": 1,
            "inteligencia": 1,
            "sabedoria": 1,
            "carisma": 1,
            "imagem": pygame.image.load("imagens/monstro.png"),
            "ca": 1,
            "vida_maxima": 1,
            "vida_atual": 1,
            "tamanho": "Grande",
            "tipo": "Reptil",
            "experiencia": 1,
        }
        self.cria_novo_monstro(dados)

    def pega_monstro_por_id(self) -> Monstro:
        if self.__monstros:
            valores_validos = [monstro.id for monstro in self.__monstros]
            id = self.tela.pega_id_monstro(valores_validos)
            for monstro in self.__monstros:
                if monstro.id == id:
                    return monstro
        else:
            self.tela.lista_monstros_vazia()
            return None

    def mostra_monstros(self):
        self.tela.mostra_monstros(self.__monstros)

    def exclui_monstro(self):
        monstro = self.pega_monstro_por_id()
        try:
            remover = self.tela.confirma_remocao(monstro.nome)
        except AttributeError:
            pass
        else:
            if remover:
                self.__monstros.remove(monstro)
                self.tela.executado_com_sucesso()

    def ataca_jogador(self):
        atacante = self.pega_monstro_por_id()
        if not atacante:
            return
        defensor = self.controlador_jogador.pega_jogador_por_id()
        if not defensor:
            return

        dano = self.tela.pega_dano()
        atacante.dano_causado.append(dano)
        defensor.dano_sofrido.append(dano)
        defensor.vida_atual -= dano

        dados = {
            "atacante": atacante.nome,
            "defensor": defensor.nome,
            "dano": dano
        }
        self.__controlador_relatorio.registra_combate(**dados)
        self.tela.resumo_combate(**dados)

    def mostra_atributos_do_monstro(self):
        monstro = self.pega_monstro_por_id()
        if monstro:
            atributos = {
                "id": monstro.id,
                "nome": monstro.nome,
                "tipo": monstro.tipo,
                "forca": monstro.forca,
                "destreza": monstro.destreza,
                "constituicao": monstro.constituicao,
                "inteligencia": monstro.inteligencia,
                "sabedoria": monstro.sabedoria,
                "carisma": monstro.carisma,
                "ca": monstro.ca,
                "ataques_monstro": [ataque.nome for ataque in monstro.ataques if monstro.ataques],
                "vida_maxima": monstro.vida_maxima,
                "vida_atual": monstro.vida_atual,
                "dano_causado": monstro.dano_causado,
                "dano_sofrido": monstro.dano_sofrido,
                "tamanho": monstro.tamanho,
            }
            self.tela.mostra_atributos(atributos)

    def lanca_magia(self):
        print("A Lanca Magia em B")
        pass

    def mostra_tela(self):

        funcoes = {
            1: self.cria_novo_monstro,
            2: self.mostra_monstros,
            3: self.exclui_monstro,
            4: self.mostra_atributos_do_monstro,
            9: self.ataca_jogador,
            13: self.lanca_magia,
            77: self.cria_monstro_teste,
        }

        super(ControladorMonstro, self).mostra_tela(funcoes)

    def mapa_moveu(self, x: int, y: int):
        for i in range(len(self.__monstros)):
            posicao = self.__monstros[i].posicao
            self.__monstros[i].posicao(posicao[0] - x, posicao[1] - y)

    @controlador_jogador.setter
    def controlador_jogador(self, value):
        self._controlador_jogador = value
