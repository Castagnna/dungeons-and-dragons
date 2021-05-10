import random
import pygame

from limite.telaImagem import TelaImagem
from limite.telaMonstro import TelaMonstro
from limite.telaPersonagemRemove import TelaPersonagemRemove
from limite.telaPersonagemTamanho import TelaPersonagemTamanho
from limite.telaPersonagemMovimentar import TelaPersonagemMovimentar
from limite.telaMonstroMostraAtributos import TelaMonstroMostraAtributos
from limite.telaPersonagemLista import TelaPersonagemLista
from limite.telaMonstroAtaque import TelaMonstroAtaque
from limite.telaMonstroNovo import TelaMonstroNovo
from limite.telaMonstroPega import TelaMonstroPega
from limite.telaMonstroAlterar import TelaMonstroAlterar

from excecao.tamanhoinvalidoException import TamanhoInvalidoException
from excecao.valoresInvalidosException import ValoresInvalidosException

from entidade.monstro import Monstro

from dao.monstroDAO import MonstroDAO
from dao.monstroContadorDAO import MonstroContadorDAO


class ControladorMonstro:
    def __init__(self, controlador_principal):
        self.__tela = TelaMonstro(self)
        self.__tela_remove = TelaPersonagemRemove(self)
        self.__tela_tamanho = TelaPersonagemTamanho(self)
        self.__tela_movimentar = TelaPersonagemMovimentar(self)
        self.__tela_imagem = TelaImagem(self)
        self.__tela_lista = TelaPersonagemLista(self)
        self.__tela_ataques = TelaMonstroAtaque(self)
        self.__tela_mostra_atributos = TelaMonstroMostraAtributos(self)
        self.__tela_novo = TelaMonstroNovo(self)
        self.__tela_pega = TelaMonstroPega(self)
        self.__tela_altera = TelaMonstroAlterar(self)
        self.__controlador_principal = controlador_principal
        self.__controlador_relatorio = controlador_principal.controlador_relatorio
        self.__controlador_ataque_monstro = controlador_principal.controlador_ataque_monstro
        self.__controlador_jogador = controlador_principal.controlador_jogador
        self.__dao = MonstroDAO()
        self.__dao_contador = MonstroContadorDAO()
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
    def controlador_ataque_monstro(self):
        return self.__controlador_ataque_monstro

    @property
    def controlador_jogador(self):
        return self.__controlador_jogador

    @property
    def monstros(self):
        return self.__dao.get_all()

    """
    setters
    """

    """
    methods
    """

    def cria_novo_monstro(self, evento='CONFIRMAR', valores: dict=None):
        tamanhos_validos = ['MIUDO', 'PEQUENO', 'MEDIO', 'GRANDE', 'ENORME', 'COLOSSAL']
        if not valores:
            evento, valores = self.__tela_novo.mostra_tela()
        if evento == 'CONFIRMAR':
            while True:
                try:
                    if valores['NOME'] == '' or valores['TIPO'] == '':
                        raise ValoresInvalidosException
                    elif valores['TAMANHO'].upper() not in tamanhos_validos:
                        raise TamanhoInvalidoException
                    else:
                        monstro = Monstro(
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
                            tipo=valores['TIPO'],
                            experiencia=int(valores['EXPERIENCIA'])
                        )
                        self.__dao.add(monstro)
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

        self.__tela_novo.fecha_tela()
        self.controlador_principal.atualizar_visualizacao()

    def cria_monstro_teste(self):
        dados = {
            "NOME": f"dragao {self.__dao_contador.get() + 1}",
            "FORCA": 1,
            "DESTREZA": 1,
            "CONSTITUICAO": 1,
            "INTELIGENCIA": 1,
            "SABEDORIA": 1,
            "CARISMA": 1,
            "IMAGEM": "Ankheg",
            "CA": 1,
            "VIDA_MAXIMA": 1,
            "VIDA_ATUAL": 1,
            "TAMANHO": "Grande",
            "TIPO": "Reptil",
            "EXPERIENCIA": 1,
        }
        self.cria_novo_monstro('CONFIRMAR',dados)

    @staticmethod
    def ordena_valores_do_dicionario_pela_chave(dicionario: dict):
        lista_ordenada = []
        for key in sorted(dicionario.keys()):
            lista_ordenada.append(dicionario[key])
        return lista_ordenada

    def pega_monstro_por_id(self):
        lista_ordenada_de_monstros = self.ordena_valores_do_dicionario_pela_chave(self.__dao.get_dao())
        mostra_tela = True
        while mostra_tela:
            evento, valores = self.__tela_pega.mostra_tela(lista_ordenada_de_monstros)
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

    def mostra_monstros(self):
        lista_ordenada_de_monstros = self.ordena_valores_do_dicionario_pela_chave(self.__dao.get_dao())

        evento, _ = self.__tela_lista.mostra_tela(lista_ordenada_de_monstros)
        if evento == 'OK':
            self.__tela_lista.fecha_tela()

    def remove_monstro(self):
        monstro = self.pega_monstro_por_id()

        if not monstro:
            return

        try:
            self.__dao.remove(monstro)
            self.__tela_remove.popup_sucesso()
            self.__tela_remove.fecha_tela()
        except KeyError:
            self.__tela_remove.popup_falha(mensagem='Jogador nao encontrado')
            self.__tela_remove.fecha_tela()

    def pega_ataque_do_monstro_por_id(self, monstro: Monstro):
        if isinstance(monstro, Monstro):
            ataques_monstro = []
            for ataque in monstro.ataques:
                ataques_monstro.append(ataque)
            botao ,valor = self.__tela_ataques.mostra_tela(ataques_monstro)
            if botao == 'CONFIRMA':
                for ataque in monstro.ataques:
                    if int(valor['ID']) == ataque.id:
                        saida = ataque
                        self.__tela_ataques.fecha_tela()
                        return saida
            else:
                self.__tela_ataques.fecha_tela()
                return None

    def ataca_jogador(self):
        atacante = self.pega_monstro_por_id()
        if not atacante:
            return
        ataque = self.pega_ataque_do_monstro_por_id(atacante)
        if not ataque:
            return
        defensor = self.controlador_jogador.pega_jogador_por_id()
        if not defensor:
            return
        dano = 0
        if ataque.teste == 'Nenhum':
            if (random.randint(1, 20) + ataque.acerto) > defensor.ca:
                for i in range(ataque.quantidade_dado):
                    dano += random.randint(1, ataque.numero_faces)
        else:
            if ataque.teste == 'Forca':
                modificador = defensor.mod_forca
            elif ataque.teste == 'Destreza':
                modificador = defensor.mod_destreza
            elif ataque.teste == 'Constituicao':
                modificador = defensor.mod_constituicao
            elif ataque.teste == 'Sabedoria':
                modificador = defensor.mod_sabedoria
            elif ataque.teste == 'Inteligencia':
                modificador = defensor.mod_inteligencia
            else:
                modificador = defensor.mod_carisma
            if (random.randint(1, 20) + modificador) < ataque.cd:
                for i in range(ataque.quantidade_dado):
                    dano += random.randint(1, ataque.numero_faces)
        dano += ataque.dano_bonus
        atacante.dano_causado.append(dano)
        defensor.dano_sofrido.append(dano)
        defensor.vida_atual -= dano
        if defensor.vida_atual <= 0:
            defensor.esta_vivo = False

        dados = {
            "atacante": atacante,
            "defensor": defensor,
            "dano": dano
        }
        mensagem = '{0} causou {1} em {2}'.format(atacante.nome, dano, defensor.nome)
        self.__controlador_relatorio.registra_combate(**dados)
        self.__tela.popup_sucesso(mensagem=mensagem)

    def mostra_atributos_do_monstro(self):
        monstro = self.pega_monstro_por_id()
        if monstro:
            atributos = {
                "ID": monstro.id,
                "nome": monstro.nome,
                "forca": monstro.forca,
                "destreza": monstro.destreza,
                "constituicao": monstro.constituicao,
                "inteligencia": monstro.inteligencia,
                "sabedoria": monstro.sabedoria,
                "carisma": monstro.carisma,
                "CA": monstro.ca,
                "imagem": monstro.imagem,
                "tamanho": monstro.tamanho,
                "tipo": monstro.tipo,
                "vida_maxima": monstro.vida_maxima,
                "vida_atual": monstro.vida_atual,
                'experiencia': monstro.experiencia
            }
            botao, _ = self.__tela_mostra_atributos.mostra_atributos_do_personagem(atributos)
            if botao:
                self.__tela_mostra_atributos.fecha_tela()

    def mostra_tela(self):
        evento, _ = self.__tela.mostra_tela()

        if evento == 'VOLTAR':
            self.__tela.fecha_tela()
            self.__controlador_principal.mostra_tela()

        funcoes = {
            'NOVO_MONSTRO': self.cria_novo_monstro,
            'LISTA_MONSTROS': self.mostra_monstros,
            'EXCLUIR_MONSTRO': self.remove_monstro,
            'CADASTRA_ATAQUE': self.cadastra_ataque_monstro,
            'EXCLUIR_ATAQUE': self.exclui_ataque_monstro,
            'ATACAR_JOGADOR': self.ataca_jogador,
            'MOVIMENTAR_MONSTRO': self.movimentar_monstro,
            'MOSTRA_ATRIBUTOS_MONSTRO': self.mostra_atributos_do_monstro,
            'CRIA_MONSTRO_TESTE': self.cria_monstro_teste
        }
        try:
            self.__tela.fecha_tela()
            funcoes[evento]()
            self.mostra_tela()
        except KeyError:
            pass

    def mapa_moveu(self, x: int, y: int):
        for i in range(len(self.__dao.get_all())):
            posicao = self.__dao.get_all()[i].posicao
            self.__dao.get_all()[i].posicao(posicao[0] - x, posicao[1] - y)

    def mostra_imagem(self, monstro):
        return monstro.imagem

    def mostra_posicao(self, monstro):
        return monstro.posicao

    @controlador_jogador.setter
    def controlador_jogador(self, value):
        if isinstance(value, ControladorJogador):
            self._controlador_jogador = value

    def altera_atributo_do_monstro(self):
        monstro = self.pega_monstro_por_id()

        if not isinstance(monstro, Monstro):
            self.__tela_altera.fecha_tela()

        dados = {
            'ID': monstro.id,
            'NOME': monstro.nome,
            'FORCA': monstro.forca,
            'DESTREZA': monstro.destreza,
            'CONSTITUICAO': monstro.constituicao,
            'INTELIGENCIA': monstro.inteligencia,
            'SABEDORIA': monstro.sabedoria,
            'CARISMA': monstro.carisma,
            'IMAGEM': monstro.imagem,
            'CA': monstro.ca,
            'VIDA_MAXIMA': monstro.vida_maxima,
            'VIDA_ATUAL': monstro.vida_atual,
            'TAMANHO': monstro.tamanho,
            'TIPO': monstro.tipo,
            'EXPERIENCIA': monstro.experiencia
        }
        evento, valores = self.__tela_altera.mostra_tela(dados)

        if evento == 'CONFIRMA':
            monstro.nome = valores['NOME']
            monstro.forca = valores['FORCA']
            monstro.destreza = valores['DESTREZA']
            monstro.constituicao = valores['CONSTITUICAO']
            monstro.inteligencia = valores['INTELIGENCIA']
            monstro.sabedoria = valores['SABEDORIA']
            monstro.carisma = valores['CARISMA']
            monstro.imagem = valores['IMAGEM']
            monstro.ca = valores['CA']
            monstro.vida_maxima = valores['VIDA_MAXIMA']
            monstro.vida_atual = valores['VIDA_ATUAL']
            monstro.tamanho = valores['TAMANHO']
            monstro.tipo = valores['TIPO']
            monstro.experiencia = valores['EXPERIENCIA']

        self.__tela_altera.fecha_tela()

    def movimentar_monstro(self):
        monstro = self.pega_monstro_por_id()
        if not monstro:
            return
        _, valores = self.__tela_movimentar.mostra_tela()
        if valores['X'] not in self.__dicio_letras.keys() and valores['Y'] not in self.__dicio_numeros.keys():
            self.__tela_movimentar.popup_falha(mensagem='Valor invalido, favor informar calores correspondetes a lateral da tela')
        else:
            posicao = [valores['X'], valores['Y']]
            monstro.movimentar(posicao)
            self.controlador_principal.atualizar_visualizacao()

    def mostra_ataques_do_monstro(self, monstro: Monstro = None):
        if not monstro:
            monstro = self.pega_monstro_por_id()
        atributos_ataques = []
        if monstro and monstro.ataques:
            for ataque in monstro.ataques:
                atributos_ataques.append([
                    str(ataque.id),
                    str(ataque.nome),
                    str(ataque.quantidade_dado),
                    str(ataque.numero_faces),
                    str(ataque.dano_bonus),
                    str(ataque.acerto),
                    str(ataque.cd),
                    str(ataque.teste)
                ])
            self.__tela_ataques.mostra_ataques(atributos_ataques)


    def cadastra_ataque_monstro(self):
        monstro = self.pega_monstro_por_id()
        if not monstro:
            return
        ataque = self.__controlador_ataque_monstro.pega_ataque_por_id()
        if not ataque:
            return
        if not (ataque in monstro.ataques):
            monstro.inserir_ataque(ataque)
            self.__tela.popup_sucesso()

    def exclui_ataque_monstro(self):
        monstro = self.pega_monstro_por_id()
        if not monstro:
            return
        ataque = self.pega_ataque_do_monstro_por_id(monstro)
        if ataque:
            monstro.remover_ataque(ataque)
            self.__tela.popup_sucesso()
