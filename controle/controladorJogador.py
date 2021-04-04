from controle.controladorGenerico import ControladorGenerico
from controle.controladorMonstro import ControladorMonstro
from controle.controladorMagia import ControladorMagia
from limite.telaJogador import TelaJogador
from entidade.jogador import Jogador
from entidade.magia import Magia
import pygame


class ControladorJogador(ControladorGenerico):
    def __init__(self, controlador_principal):
        super(ControladorJogador, self).__init__(TelaJogador(self))
        self.__controlador_principal = controlador_principal
        self.__controlador_arma = controlador_principal.controlador_arma
        self.__controlador_monstro = None
        self.__controlador_magia = ControladorMagia(self)
        self.__jogadores = []
        self.__counta_jogadores = 1

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

    @property
    def controlador_magia(self):
        return self.__controlador_magia

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
        if isinstance(controlador_monstro, ControladorMonstro):
            if controlador_monstro != self.__controlador_monstro:
                self.__controlador_monstro = controlador_monstro
            if self != controlador_monstro.controlador_jogador:
                controlador_monstro.controlador_jogador = self

    def cria_novo_jogador(self, dados: dict = None):
        if not dados:
            dados = self.tela.pega_dados_do_jogador()

        if dados['tamanho'] == 'Grande':
            dados['imagem'] = pygame.transform.scale(dados['imagem'], (200, 200))
        elif dados['tamanho'] == 'Enorme':
            dados['imagem'] = pygame.transform.scale(dados['imagem'], (300, 300))
        elif dados['tamanho'] == 'Colossal':
            dados['imagem'] = pygame.transform.scale(dados['imagem'], (400, 400))
        else:
            dados['imagem'] = pygame.transform.scale(dados['imagem'], (100, 100))
        dados['posicao'] = dados['imagem'].get_rect()
        dados['posicao'][0] = 100 * (self.__counta_jogadores % 10)
        dados['posicao'][1] = 100 * (self.__counta_jogadores // 10)

        novo_jogador = Jogador(
            id=self.__counta_jogadores,
            **dados
        )
        self.__counta_jogadores += 1
        self.__jogadores.append(novo_jogador)
        self.tela.executado_com_sucesso()

    def cria_jogador_teste(self):
        dados = {
            "nome": f"Fulano {self.__counta_jogadores}",
            "forca": 10,
            "destreza": 10,
            "constituicao": 10,
            "inteligencia": 10,
            "sabedoria": 10,
            "carisma": 10,
            "imagem": pygame.image.load("imagens/jogador.png"),
            "ca": 10,
            "vida_maxima": 10,
            "vida_atual": 10,
            "tamanho": "Pequeno",
            "nome_jogador": "daniel",
            "level": 1,
            "experiencia": 1,
        }
        self.cria_novo_jogador(dados)

    def mostra_jogadores(self):
        self.tela.mostra_jogadores(self.__jogadores)

    def pega_jogador_por_id(self) -> Jogador:
        if self.__jogadores:
            valores_validos = [jogador.id for jogador in self.__jogadores]
            id = self.tela.pega_id_jogador(valores_validos)
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
        jogador = self.pega_jogador_por_id()
        if jogador:
            atributos = {
                "id": jogador.id,
                "nome": jogador.nome,
                "forca": jogador.forca,
                "destreza": jogador.destreza,
                "constituicao": jogador.constituicao,
                "inteligencia": jogador.inteligencia,
                "sabedoria": jogador.sabedoria,
                "carisma": jogador.carisma,
                "ca": jogador.ca,
                "armas": [arma.nome for arma in jogador.armas if jogador.armas],
                "magias": [magia.nome for magia in jogador.magias if jogador.magias],
                "vida_maxima": jogador.vida_maxima,
                "vida_atual": jogador.vida_atual,
                "tamanho": jogador.tamanho,
                "nome_jogador": jogador.nome_jogador,
                "level": jogador.level,
                "experiencia": jogador.experiencia,
            }
            self.tela.mostra_atributos(atributos)

    def altera_atributo_do_jogador(self):
        pass

    def equipa_arma(self):
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

    def mostra_armas_do_jogador(self, jogador: Jogador = None):

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
                self.tela.mostra_arma_do_jogador(
                    **atributos_arma,
                    mostra_titulo=mostra_titulo
                )
                mostra_titulo = False

    def pega_arma_do_jogador_por_id(self, jogador: Jogador):
        self.mostra_armas_do_jogador(jogador)
        if jogador.armas:
            id_para_arma = {arma.id: arma for arma in jogador.armas}
            id = self.tela.pega_id(id_para_arma.keys())
            return id_para_arma[id]

    def desequipa_arma(self):
        self.mostra_jogadores()
        jogador = self.pega_jogador_por_id()
        if not jogador:
            return
        arma = self.pega_arma_do_jogador_por_id(jogador)
        if arma:
            jogador.remove_arma(arma)
            self.tela.executado_com_sucesso()

    def ataca_monstro(self):
        atacante = self.pega_jogador_por_id()
        if not atacante:
            return
        defensor = self.controlador_monstro.pega_monstro_por_id()
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

        self.tela.resumo_combate(**dados)

    def vincula_magia(self):
        self.tela.cria_magia()
        magia = self.__controlador_magia.cria_magia()

        self.tela.jogador_da_magia()
        jogador = self.pega_jogador_por_id()

        if self.tela.confirma_vincular(magia.nome, jogador.nome):
            jogador.vincula_magia(magia)
            self.tela.executado_com_sucesso()

    def pega_magia_por_id(self, jogador: Jogador) -> Magia:
        self.mostra_magias_do_jogador(jogador)
        if jogador.magias:
            id_para_magia = {magia.id: magia for magia in jogador.magias}
            id = self.tela.pega_id(id_para_magia.keys())
            return id_para_magia[id]

    def desvincula_magia(self):

        self.tela.jogador_da_magia()
        jogador = self.pega_jogador_por_id()

        magia = self.pega_magia_por_id(jogador)

        if self.tela.confirma_desvincular():
            jogador.desvincula_magia(magia)
        self.tela.executado_com_sucesso()

    def mostra_magias_do_jogador(self, jogador: Jogador = None):

        if not jogador:
            jogador = self.pega_jogador_por_id()

        if jogador and jogador.magias:
            mostra_titulo = True
            for magia in jogador.magias:
                atributos_magia = {
                    "id": magia.id,
                    "nome": magia.nome,
                    "quantidade_dado": magia.quantidade_dado,
                    "numero_faces": magia.numero_faces
                }
                self.tela.mostra_magia_do_jogador(
                    **atributos_magia,
                    mostra_titulo=mostra_titulo
                )
                mostra_titulo = False

    def lanca_magia_no_monstro(self):
        pass

    def mostra_tela(self):

        funcoes = {
            1: self.cria_novo_jogador,
            2: self.mostra_jogadores,
            3: self.remove_jogador,
            4: self.mostra_atributos_do_jogador,
            5: self.altera_atributo_do_jogador,
            6: self.equipa_arma,
            7: self.desequipa_arma,
            8: self.mostra_armas_do_jogador,
            9: self.ataca_monstro,
            10: self.vincula_magia,
            11: self.desvincula_magia,
            12: self.mostra_magias_do_jogador,
            13: self.lanca_magia_no_monstro,
            77: self.cria_jogador_teste,
        }

        super(ControladorJogador, self).mostra_tela(funcoes)

    def mapa_moveu(self, x: int, y: int):
        for i in range(len(self.__jogadores)):
            posicao = self.__jogadores[i].posicao
            self.__jogadores[i].posicao(posicao[0] - x, posicao[1] - y)
