import random
import pygame

from excecao.tamanhoinvalidoException import TamanhoInvalidoException
from excecao.valoresInvalidosException import ValoresInvalidosException

from controle.controladorMonstro import ControladorMonstro
from controle.controladorMagia import ControladorMagia

from limite.telaJogador import TelaJogador
from limite.telaJogadorNovo import TelaJogadorNovo
from limite.telaJogadorPega import TelaJogadorPega
from limite.telaJogadorMostraArmas import TelaJogadorMostraArmas
from limite.telaJogadorMostraAtributos import TelaJogadorMostraAtributos
from limite.telaPersonagemRemove import TelaPersonagemRemove
from limite.telaPersonagemTamanho import TelaPersonagemTamanho
from limite.telaPersonagemMovimentar import TelaPersonagemMovimentar
from limite.telaPersonagemLista import TelaPersonagemLista
from limite.telaJogadorArmas import TelaJogadorArmas
from limite.telaJogadorAlterar import TelaJogadorAlterar
from limite.telaImagem import TelaImagem

from entidade.jogador import Jogador
from entidade.magia import Magia

from dao.jogadorDAO import JogadorDAO
from dao.jogadorContadorDAO import JogadorContadorDAO



class ControladorJogador:
    def __init__(self, controlador_principal):
        self.__tela = TelaJogador(self)
        self.__tela_pega = TelaJogadorPega(self)
        self.__tela_remove = TelaPersonagemRemove(self)
        self.__tela_imagem = TelaImagem(self)
        self.__tela_lista = TelaPersonagemLista(self)
        self.__tela_armas = TelaJogadorArmas(self)
        self.__tela_movimentar = TelaPersonagemMovimentar(self)
        self.__tela_tamanho = TelaPersonagemTamanho(self)
        self.__tela_novo = TelaJogadorNovo(self)
        self.__tela_altera = TelaJogadorAlterar(self)
        self.__tela_mostra_armas = TelaJogadorMostraArmas(self)
        self.__tela_mostra_atributos = TelaJogadorMostraAtributos(self)
        self.__controlador_principal = controlador_principal
        self.__controlador_relatorio = controlador_principal.controlador_relatorio
        self.__controlador_arma = controlador_principal.controlador_arma
        self.__controlador_monstro = None
        self.__controlador_magia = ControladorMagia(self)
        self.__dao = JogadorDAO()
        self.__dao_contador = JogadorContadorDAO()
        self.__dicio_letras = {'A': 100, 'B': 200, 'C': 300, 'D': 400, 'E': 500,
                               'F': 600, 'G': 700, 'H': 800, 'I': 900, 'J': 1000,
                               'K': 1100, 'L': 1200, 'M': 1300, 'N': 1400, 'O': 1500,
                               'P': 1600, 'Q': 1700, 'R': 1800, 'S': 1900,
                               'T': 2000, 'U': 2100, 'V': 2200, 'W': 2300,
                               'X': 2400, 'Y': 2500, 'Z': 2500}
        self.__dicio_numeros = {'1': 100, '2': 200, '3': 300, '4': 400, '5': 500, '6': 600, '7': 700, '8': 800,
                                '9': 900}

    """
    getters
    """

    @property
    def controlador_principal(self):
        return self.__controlador_principal

    @property
    def jogadores(self):
        return self.__dao.get_all()

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

    def cria_novo_jogador(self, evento='CONFIRMAR', valores: dict=None):
        tamanhos_validos = ['MIUDO', 'PEQUENO', 'MEDIO', 'GRANDE', 'ENORME', 'COLOSSAL']
        if not valores:
            evento, valores = self.__tela_novo.mostra_tela()
        if evento == 'CONFIRMAR':
            while True:
                try:
                    if valores['NOME'] == '' or valores['PLAYER'] == '':
                        raise ValoresInvalidosException
                    elif valores['TAMANHO'].upper() not in tamanhos_validos:
                        raise TamanhoInvalidoException

                    else:
                        jogador = Jogador(
                            id=self.__dao_contador.get() + 1,
                            nome=valores['NOME'],
                            forca=int(valores['FORCA']),
                            destreza=int(valores['DESTREZA']),
                            constituicao=int(valores['CONSTITUICAO']),
                            inteligencia=int(valores['INTELIGENCIA']),
                            sabedoria=int(valores['SABEDORIA']),
                            carisma=int(valores['CARISMA']),
                            imagem=valores['IMAGEM'],
                            ca=valores['CA'],
                            vida_maxima=int(valores['VIDA_MAXIMA']),
                            vida_atual=int(valores['VIDA_ATUAL']),
                            tamanho=valores['TAMANHO'],
                            nome_jogador=valores['PLAYER'],
                            level=valores['LEVEL'],
                            experiencia=int(valores['EXPERIENCIA']),
                            proficiencia=int(valores['PROFICIENCIA']),
                            cd=int(valores['CD'])
                            )
                        self.__dao.add(jogador)
                        self.__dao_contador.add(1)
                        self.__tela_novo.popup_sucesso()
                        break
                except ValoresInvalidosException:
                    self.__tela_novo.popup_falha(mensagem='Favor preencher todos os valores')
                    self.__tela_novo.fecha_tela()
                    evento, valores = self.__tela_novo.mostra_tela()
                    if evento != 'CONFIRMAR':
                        break

                except TamanhoInvalidoException:
                    evento, valor = self.__tela_tamanho.mostra_tela()
                    valores['TAMANHO'] = valor['TAMANHO']
                    self.__tela_tamanho.fecha_tela()
                    if evento != 'CONFIRMAR':
                        break

                except FileNotFoundError:
                    evento, valor = self.__tela_imagem.mostra_tela()
                    valores['IMAGEM'] = valor['IMAGEM']
                    self.__tela_imagem.fecha_tela()
                    if evento != 'CONFIRMAR':
                        break
        else:
            self.__tela_novo.popup_sucesso(mensagem='Operacao cancelada')
        self.__tela_novo.fecha_tela()
        self.controlador_principal.atualizar_visualizacao()

    def cria_jogador_teste(self):
        dados = {
            "NOME": f"Fulano {self.__dao_contador.get() + 1}",
            "FORCA": 10,
            "DESTREZA": 10,
            "CONSTITUICAO": 10,
            "INTELIGENCIA": 10,
            "SABEDORIA": 10,
            "CARISMA": 10,
            "CA": 10,
            "IMAGEM": "Anao_Barbaro",
            "VIDA_MAXIMA": 10,
            "VIDA_ATUAL": 10,
            "TAMANHO": "Pequeno",
            "PLAYER": "daniel",
            "LEVEL": 1,
            "EXPERIENCIA": 1,
            "PROFICIENCIA": 3,
            "CD": 12
        }
        self.cria_novo_jogador('CONFIRMAR', dados)

    def mostra_jogadores(self):
        lista_ordenada_de_jogadores = self.ordena_valores_do_dicionario_pela_chave(self.__dao.get_dao())

        evento, _ = self.__tela_lista.mostra_tela(lista_ordenada_de_jogadores)
        if evento == 'OK':
            self.__tela_lista.fecha_tela()

    def mostra_atributos_do_jogador(self):
        jogador = self.pega_jogador_por_id()
        if jogador:
            atributos = {
                'ID': jogador.id,
                'nome': jogador.nome,
                'imagem': jogador.imagem,
                'forca': jogador.forca,
                'destreza': jogador.destreza,
                'constituicao': jogador.constituicao,
                'inteligencia': jogador.inteligencia,
                'sabedoria': jogador.sabedoria,
                'carisma': jogador.carisma,
                'CA': jogador.ca,
                'vida_maxima': jogador.vida_maxima,
                'vida_atual': jogador.vida_atual,
                'tamanho': jogador.tamanho,
                'player': jogador.nome_jogador,
                'level': jogador.level,
                'experiencia': jogador.experiencia,
                'proficiencia': jogador.proficiencia,
                'CD': jogador.cd
            }
            botao, _ = self.__tela_mostra_atributos.mostra_atributos_do_personagem(atributos)
            if botao:
                self.__tela_mostra_atributos.fecha_tela()

    def ordena_valores_do_dicionario_pela_chave(self, dicionario: dict):
        lista_ordenada = []
        for key in sorted(dicionario.keys()):
            lista_ordenada.append(dicionario[key])
        return lista_ordenada

    def pega_jogador_por_id(self):
        lista_ordenada_de_jogadores = self.ordena_valores_do_dicionario_pela_chave(self.__dao.get_dao())
        mostra_tela = True
        while mostra_tela:
            evento, valores = self.__tela_pega.mostra_tela(lista_ordenada_de_jogadores)
            if evento == 'CONFIRMAR':
                try:
                    id = int(valores['ID'])
                    nome = self.__dao.get(id)
                    mostra_tela = False
                    self.__tela_pega.fecha_tela()
                    return nome
                except ValueError:
                    self.__tela_pega.popup_falha(mensagem='O valor precisa ser inteiro')
                    self.__tela_pega.fecha_tela()
            elif evento == 'CANCELA' or evento == None:
                mostra_tela = False
                self.__tela_pega.fecha_tela()

    def remove_jogador(self):

        jogador = self.pega_jogador_por_id()

        if not jogador:
            return

        try:
            self.__dao.remove(jogador)
            self.__tela_remove.popup_sucesso()
            self.__tela_remove.fecha_tela()
        except KeyError:
            self.__tela_remove.popup_falha(mensagem='Jogador nao encontrado')
            self.__tela_remove.fecha_tela()

    def altera_atributo_do_jogador(self):
        jogador = self.pega_jogador_por_id()

        if not isinstance(jogador, Jogador):
            self.__tela_altera.fecha_tela()

        dados = {
            'ID': jogador.id,
            'NOME': jogador.nome,
            'FORCA': jogador.forca,
            'DESTREZA': jogador.destreza,
            'CONSTITUICAO': jogador.constituicao,
            'INTELIGENCIA': jogador.inteligencia,
            'SABEDORIA': jogador.sabedoria,
            'CARISMA': jogador.carisma,
            'IMAGEM': jogador.imagem,
            'CA': jogador.ca,
            'VIDA_MAXIMA': jogador.vida_maxima,
            'VIDA_ATUAL': jogador.vida_atual,
            'TAMANHO': jogador.tamanho,
            'PLAYER': jogador.nome_jogador,
            'LEVEL': jogador.level,
            'EXPERIENCIA': jogador.experiencia,
            'PROFICIENCIA': jogador.proficiencia,
            'CD': jogador.cd
        }

        evento, valores = self.__tela_altera.mostra_tela(dados)

        if evento == 'CONFIRMA':
            jogador.nome = valores['NOME']
            jogador.forca = int(valores['FORCA'])
            jogador.destreza = int(valores['DESTREZA'])
            jogador.constituicao = int(valores['CONSTITUICAO'])
            jogador.inteligencia = int(valores['INTELIGENCIA'])
            jogador.sabedoria = int(valores['SABEDORIA'])
            jogador.carisma = int(valores['CARISMA'])
            jogador.imagem = valores['IMAGEM']
            jogador.ca = int(valores['CA'])
            jogador.vida_maxima = int(valores['VIDA_MAXIMA'])
            jogador.vida_atual = int(valores['VIDA_ATUAL'])
            jogador.tamanho = valores['TAMANHO']
            jogador.nome_jogador = valores['PLAYER']
            jogador.level = int(valores['LEVEL'])
            jogador.experiencia = int(valores['EXPERIENCIA'])
            jogador.proficiencia = int(valores['PROFICIENCIA'])
            jogador.cd = int(valores['CD'])

        self.__tela_altera.fecha_tela()

    def mostra_tela(self):
        evento, _ = self.__tela.mostra_tela()

        if evento == 'VOLTAR' or evento == None:
            self.__tela.fecha_tela()
            self.__controlador_principal.mostra_tela()

        funcoes = {
            'NOVO_JOGADOR': self.cria_novo_jogador,
            'MOSTRA_JOGADORES': self.mostra_jogadores,
            'REMOVE_JOGADOR': self.remove_jogador,
            'ATRIBUTOS_JOGADOR': self.mostra_atributos_do_jogador,
            'ALTERA_ATRIBUTOS_JOGADOR': self.altera_atributo_do_jogador,
            'EQUIPA_ARMA': self.equipa_arma,
            'DESEQUIPA_ARMA': self.desequipa_arma,
            'MOSTRA_ARMAS': self.mostra_armas_do_jogador,
            'ATACA_MONSTRO': self.ataca_monstro,
            'VINCULA_MAGIA': self.vincula_magia,
            'DESVINCULA_MAGIA': self.desvincula_magia,
            'MOSTRA_MAGIAS': self.mostra_magias_do_jogador,
            'ALTERA_ATRIBUTOS_MAGIA': self.altera_atributo_da_magia,
            'LANCA_MAGIA': self.lanca_magia_no_monstro,
            'MOVIMENTAR_JOGADOR': self.movimentar_jogador,
            'CRIA_JOGADOR_TESTE': self.cria_jogador_teste,
        }
        try:
            self.__tela.fecha_tela()
            funcoes[evento]()
            self.mostra_tela()
        except KeyError:
            return

    def equipa_arma(self):
        jogador = self.pega_jogador_por_id()
        if not jogador:
            return
        arma = self.__controlador_arma.pega_arma_por_id()
        if not arma:
            return
        if not (arma in jogador.armas):
            jogador.adiciona_arma(arma)
            self.__tela.popup_sucesso()

    def mostra_armas_do_jogador(self, jogador: Jogador = None):

        if not jogador:
            jogador = self.pega_jogador_por_id()

        if jogador and jogador.armas:
            atributos_arma = []
            for arma in jogador.armas:
                atributos_arma.append([arma.id, arma.nome])
            self.__tela_mostra_armas.mostra_armas_do_jogador(atributos_arma)

    def pega_arma_do_jogador_por_id(self, jogador: Jogador):
        if jogador.armas:
            armas_jogador = []
            for arma in jogador.armas:
                armas_jogador.append([arma.id, arma.nome])
            _, valor = self.__tela_armas.mostra_ataques(armas_jogador)
            return int(valor)

    def desequipa_arma(self):
        #self.mostra_jogadores()
        jogador = self.pega_jogador_por_id()
        if not jogador:
            return
        arma = self.pega_arma_do_jogador_por_id(jogador)
        if arma:
            jogador.remove_arma(arma)
            self.__tela.popup_sucesso()

    def ataca_monstro(self):
        atacante = self.pega_jogador_por_id()
        if not atacante:
            return
        arma = self.pega_arma_do_jogador_por_id(atacante)
        if not arma:
            return
        defensor = self.controlador_monstro.pega_monstro_por_id()
        if not defensor:
            return
        dano = 0
        defensor.adiciona_atacante(atacante)
        if (random.randint(1, 20) + atacante.proficiencia + atacante.mod_forca) > defensor.ca:
            dano += arma.dano() + atacante.mod_forca
            atacante.dano_causado.append(dano)
            defensor.dano_sofrido.append(dano)
            defensor.vida_atual -= dano
            if defensor.vida_atual <= 0:
                defensor.esta_vivo = False
                experiencia = (defensor.experiencia // len(defensor.atacado_por))
                for jogador in defensor.atacado_por:
                    jogador.recebe_experiencia(experiencia)

        dados = {
            "atacante": atacante,
            "defensor": defensor,
            "dano": dano
        }
        mensagem = '{0} causou {1} em {2}'.format(atacante.nome, dano, defensor.nome)
        self.__controlador_relatorio.registra_combate(**dados)
        self.__tela.popup_sucesso(mensagem=mensagem)

    def vincula_magia(self):

        #self.tela.jogador_da_magia()
        jogador = self.pega_jogador_por_id()

        if not jogador:
            return None

        magia = self.__controlador_magia.cria_magia()
        if isinstance(magia, Magia):
            jogador.vincula_magia(magia)
            self.__tela.popup_sucesso()
        else:
            self.__tela.popup_sucesso(mensagem='Operacao cancelada')

    def mostra_magias_do_jogador(self, jogador: Jogador = None):

        if not jogador:
            jogador = self.pega_jogador_por_id()

        if jogador and jogador.magias:
            magias_jogador = []
            for magia in jogador.magias:
                magias_jogador.append([magia.id, magia.nome])
            self.__tela_mostra_armas.mostra_armas_do_jogador(magias_jogador)

    def pega_magia_por_id(self, jogador: Jogador) -> Magia:
        if jogador.magias:
            magias_jogador = []
            for magia in jogador.magias:
                magias_jogador.append([magia.id, magia.nome])
            _,valor = self.__tela_armas.mostra_ataques(magias_jogador)
            return int(valor)

    def desvincula_magia(self):
        jogador = self.pega_jogador_por_id()

        if not jogador:
            return None

        magia = self.pega_magia_por_id(jogador)

        if magia:
            jogador.desvincula_magia(magia)
            self.__tela.popup_sucesso()

    def lanca_magia_no_monstro(self):
        atacante = self.pega_jogador_por_id()
        if not atacante:
            return
        magia = self.pega_magia_por_id(atacante)
        if not magia:
            return
        elif atacante.get_espaco_magia(magia.circulo) <= 0:
            self.tela.espaco_magia_insu(magia.circulo)
            return
        defensor = self.controlador_monstro.pega_monstro_por_id()
        if not defensor:
            return
        atacante.set_espaco_magia(magia.circulo, atacante.get_espaco_magia(magia.circulo) - 1)
        dano = 0
        defensor.adiciona_atacante(atacante)
        modificador_magia = self.tela.pede_modificador_magia()
        if modificador_magia == 'Inteligencia':
            modificador_ataque = atacante.mod_inteligencia
        elif modificador_magia == 'Sabedoria':
            modificador_ataque = atacante.mod_sabedoria
        elif modificador_magia == 'Carisma':
            modificador_ataque = atacante.mod_carisma
        else:
            return
        defensor.adiciona_atacante(atacante)
        if magia.teste != "Nenhum":
            if (random.randint(1, 20) + modificador_ataque + atacante.proficiencia) > defensor.ca:
                for i in range(magia.quantidade_dado):
                    dano += random.randint(1, magia.numero_faces)
        else:
            if magia.teste == 'Forca':
                modificador = defensor.mod_forca
            elif magia.teste == 'Destreza':
                modificador = defensor.mod_destreza
            elif magia.teste == 'Constituicao':
                modificador = defensor.mod_constituicao
            elif magia.teste == 'Sabedoria':
                modificador = defensor.mod_sabedoria
            elif magia.teste == 'Inteligencia':
                modificador = defensor.mod_inteligencia
            elif magia.teste == 'Carisma':
                modificador = defensor.mod_carisma
            else:
                return
            if (random.randint(1, 20) + modificador) < atacante.cd:
                for i in range(magia.quantidade_dado):
                    dano += random.randint(1, magia.numero_faces)
        dano += modificador_ataque
        atacante.dano_causado.append(dano)
        defensor.dano_sofrido.append(dano)
        defensor.vida_atual -= dano
        if defensor.vida_atual <= 0:
            defensor.esta_vivo = False
            experiencia = (defensor.experiencia // len(defensor.atacado_por))
            for jogador in defensor.atacado_por:
                jogador.recebe_experiencia(experiencia)

        dados = {
            "atacante": atacante,
            "defensor": defensor,
            "dano": dano
        }
        mensagem = '{0} causou {1} em {2}'.format(atacante.nome, dano, defensor.nome)

        self.__controlador_relatorio.registra_combate(**dados)
        self.__tela.popup_sucesso(mensagem=mensagem)

    def altera_atributo_da_magia(self):
        jogador = self.pega_jogador_por_id()
        magia = self.pega_magia_por_id(jogador)
        self.controlador_magia.altera_magia(magia)

    def movimentar_jogador(self):
        jogador = self.pega_jogador_por_id()
        if not jogador:
            return
        _, valores = self.__tela_movimentar.mostra_tela()
        if valores['X'] not in self.__dicio_letras.keys() and valores['Y'] not in self.__dicio_numeros.keys():
            self.__tela_movimentar.popup_falha(mensagem='Valor invalido, favor informar calores correspondetes a lateral da tela')
        else:
            posicao = [valores['X'], valores['Y']]
            jogador.movimentar(posicao)
            self.controlador_principal.atualizar_visualizacao()

    def mostra_imagem(self, jogador):
        return jogador.imagem

    def mostra_posicao(self, jogador):
        return jogador.posicao


    def mapa_moveu(self, x: int, y: int):
        for i in range(len(self.__dao.get_all())):
            posicao = self.__dao.get_all()[i].posicao
            self.__dao.get_all()[i].posicao(posicao[0] - x, posicao[1] - y)
