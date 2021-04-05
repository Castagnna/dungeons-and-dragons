from controle.controladorGenerico import ControladorGenerico
from limite.telaMonstro import TelaMonstro
from entidade.monstro import Monstro
import random
import pygame


class ControladorMonstro(ControladorGenerico):
    def __init__(self, controlador_principal):
        super(ControladorMonstro, self).__init__(TelaMonstro(self))
        self.__controlador_principal = controlador_principal
        self.__controlador_relatorio = controlador_principal.controlador_relatorio
        self.__controlador_ataque_monstro = controlador_principal.controlador_ataque_monstro
        self.__controlador_jogador = controlador_principal.controlador_jogador
        self.__monstros = []
        self.__counta_monstros = 1

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
            dados = self.tela.pega_dados_do_monstro()
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
            "imagem": pygame.image.load("tokens/Ankheg.png"),
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

    def ataca_jogador(self): #
        atacante = self.pega_monstro_por_id()
        if not atacante:
            return
        ataque = self.pega_ataque_do_monstro_por_id(atacante)
        if not ataque:
            return
        defensor = self.controlador_jogador.pega_jogador_por_id()
        if not defensor:
            return
        dano = 10
        if ataque.teste == "Nenhum":
            if (random.randint(1, 20) + ataque.acerto) > defensor.ca:
                for i in range(ataque.quantidade_dado):
                    dano += random.randint(1, ataque.numero_faces)
                dano += ataque.dano_bonus
                atacante.dano_causado.append(dano)
                defensor.dano_sofrido.append(dano)
                defensor.vida_atual -= dano
                if defensor.vida_atual <= 0:
                    self.controlador_jogador.remover_jogador(defensor)
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
            if (random.randint(1,20) + modificador) < ataque.cd:
                for i in range(ataque.quantidade_dado):
                    dano += random.randint(1, ataque.numero_faces)
                dano += atacante.mod_forca
                atacante.dano_causado.append(dano)
                defensor.dano_sofrido.append(dano)
                defensor.vida_atual -= dano
                if defensor.vida_atual <= 0:
                    self.controlador_jogador.remover_jogador(defensor)
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
            4: self.cadastra_ataque_monstro,
            5: self.exclui_ataque_monstro,
            6: self.ataca_jogador,
            7: self.movimentar_monstro,
            8: self.mostra_atributos_do_monstro,
            9: self.ataca_jogador,
            13: self.lanca_magia,
            77: self.cria_monstro_teste
        }

        super(ControladorMonstro, self).mostra_tela(funcoes)

    def mapa_moveu(self, x: int, y: int):
        for i in range(len(self.__monstros)):
            posicao = self.__monstros[i].posicao
            self.__monstros[i].posicao(posicao[0] - x, posicao[1] - y)

    def mostra_imagem(self, monstro):
        return monstro.imagem

    def mostra_posicao(self, monstro):
        return monstro.posicao

    @controlador_jogador.setter
    def controlador_jogador(self, value):
        self._controlador_jogador = value

    def remover_monstro(self, monstro):
        self.__monstros.remove(monstro)

    def altera_atributo_do_monstro(self):
        monstro = self.pega_monstro_por_id()
        opcao = self.tela.mostra_alterar_monstro()

        funcoes = {
            1: ("nome", "str"),
            2: ("forca", "int"),
            3: ("destreza", "int"),
            4: ("constituicao", "int"),
            5: ("inteligencia", "int"),
            6: ("sabedoria", "int"),
            7: ("carisma", "int"),
            9: ("ca", "int"),
            10: ("vida_maxima", "int"),
            11: ("tamanho", "str"),
            12: ("vida_atual", "int"),
            13: ('tipo', 'str'),
            14: ("experiencia", "int")
        }
        if opcao == 8:
            novo_valor = self.tela.pega_imagem()
            if monstro.tamanho == 'Grande':
                novo_valor = pygame.transform.scale(novo_valor, (200, 200))
            elif monstro.tamanho == 'Enorme':
                novo_valor = pygame.transform.scale(novo_valor, (300, 300))
            elif monstro.tamanho == 'Colossal':
                novo_valor = pygame.transform.scale(novo_valor, (400, 400))
            else:
                novo_valor = pygame.transform.scale(novo_valor, (100, 100))
        else:
            tipo = funcoes[opcao][1]

            novo_valor = self.tela.pega_dado(
            mensagem="Entre novo valor para {}: ".format(funcoes[opcao][0]),
            tipo=tipo
            )
        if opcao == 1:
            monstro.nome = novo_valor
        elif opcao == 2:
            monstro.forca = novo_valor
        elif opcao == 3:
            monstro.destreza = novo_valor
        elif opcao == 4:
            monstro.constituicao = novo_valor
        elif opcao == 5:
            monstro.inteligencia = novo_valor
        elif opcao == 6:
            monstro.sabedoria = novo_valor
        elif opcao == 7:
            monstro.carisma = novo_valor
        elif opcao == 9:
            monstro.ca = novo_valor
        elif opcao == 10:
            monstro.vida_maxima = novo_valor
        elif opcao == 11:
            monstro.tamanho = novo_valor
        elif opcao == 12:
            monstro.vida_atual = novo_valor
        elif opcao == 13:
            monstro.tipo = novo_valor
        elif opcao == 14:
            monstro.experiencia = novo_valor

    def movimentar_monstro(self):
        monstro = self.pega_monstro_por_id()
        if not monstro:
            return
        posicao = self.tela.movimenta_monstro()
        monstro.movimentar(posicao)
        self.controlador_principal.atualizar_visualizacao()

    def cadastra_ataque_monstro(self):
        self.mostra_monstros()
        monstro = self.pega_monstro_por_id()
        if not monstro:
            return
        self.__controlador_ataque_monstro.mostra_ataques_monstro()
        ataque = self.__controlador_ataque_monstro.pega_ataque_por_id()
        if not ataque:
            return
        if not (ataque in monstro.ataques):
            monstro.inserir_ataque(ataque)
            self.tela.executado_com_sucesso()

    def pega_ataque_do_monstro_por_id(self, monstro: Monstro):
        self.mostra_ataques_do_monstro(monstro)
        if monstro.ataques:
            id_para_ataque = {ataque.id: ataque for ataque in monstro.ataques}
            id = self.tela.pega_id(id_para_ataque.keys())
            return id_para_ataque[id]

    def mostra_ataques_do_monstro(self, monstro: Monstro = None):

        if not monstro:
            monstro = self.pega_monstro_por_id()

        if monstro and monstro.ataques:
            mostra_titulo = True
            for ataque in monstro.ataques:
                atributos_ataque = {
                    "id": ataque.id,
                    "nome": ataque.nome,
                    "quantidade_dado": ataque.quantidade_dado,
                    "numero_faces": ataque.numero_faces,
                    "dano_bonus": ataque.dano_bonus,
                    "acerto": ataque.acerto,
                    "cd": ataque.cd,
                    "teste": ataque.teste
                }
                self.tela.mostra_ataque_do_monstro(
                    **atributos_ataque,
                    mostra_titulo=mostra_titulo
                )
                mostra_titulo = False

    def exclui_ataque_monstro(self):
        self.mostra_monstros()
        monstro = self.pega_monstro_por_id()
        if not monstro:
            return
        ataque = self.pega_ataque_do_monstro_por_id(monstro)
        if ataque:
            monstro.remove_arma(ataque)
            self.tela.executado_com_sucesso()

