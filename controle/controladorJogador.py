from controle.controladorGenerico import ControladorGenerico
from controle.controladorMonstro import ControladorMonstro
from controle.controladorMagia import ControladorMagia
from limite.telaJogador import TelaJogador
from entidade.jogador import Jogador
from entidade.magia import Magia
import random
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


    def cria_novo_jogador(self, dados = None):
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
        dados['posicao'][1] = 100 * ((self.__counta_jogadores * 10) // 10)

        novo_jogador = Jogador(
            id=self.__counta_jogadores,
            **dados
        )
        self.__counta_jogadores += 1
        self.__jogadores.append(novo_jogador)
        self.tela.executado_com_sucesso()
        self.controlador_principal.atualizar_visualizacao()

    def cria_jogador_teste(self):
        dados = {
            "nome": f"Fulano {self.__counta_jogadores}",
            "forca": 10,
            "destreza": 10,
            "constituicao": 10,
            "inteligencia": 10,
            "sabedoria": 10,
            "carisma": 10,
            "ca": 10,
            "imagem": pygame.image.load('tokens/Anao_Barbaro.png'),
            "vida_maxima": 10,
            "vida_atual": 10,
            "tamanho": "Pequeno",
            "nome_jogador": "daniel",
            "level": 1,
            "experiencia": 1,
            "proficiencia": 3,
            "cd": 12
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
                "proficiencia": jogador.proficiencia,
                "cd": jogador.cd
            }
            self.tela.mostra_atributos(atributos)

    def altera_atributo_do_jogador(self):
        jogador = self.pega_jogador_por_id()
        opcao = self.tela.mostra_alterar_jogador()

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
            13: ("nome_jogador", "str"),
            14: ("level", "int"),
            15: ("experiencia", "int"),
            16: ("proficiencia", "int"),
            17: ("cd", "int")
        }
        if opcao == 8:
            novo_valor = self.tela.pega_imagem()
            if jogador.tamanho == 'Grande':
                novo_valor = pygame.transform.scale(novo_valor, (200, 200))
            elif jogador.tamanho == 'Enorme':
                novo_valor = pygame.transform.scale(novo_valor, (300, 300))
            elif jogador.tamanho == 'Colossal':
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
            jogador.nome = novo_valor
        elif opcao == 2:
            jogador.forca = novo_valor
        elif opcao == 3:
            jogador.destreza = novo_valor
        elif opcao == 4:
            jogador.constituicao = novo_valor
        elif opcao == 5:
            jogador.inteligencia = novo_valor
        elif opcao == 6:
            jogador.sabedoria = novo_valor
        elif opcao == 7:
            jogador.carisma = novo_valor
        elif opcao == 9:
            jogador.ca = novo_valor
        elif opcao == 10:
            jogador.vida_maxima = novo_valor
        elif opcao == 11:
            jogador.tamanho = novo_valor
        elif opcao == 12:
            jogador.vida_atual = novo_valor
        elif opcao == 13:
            jogador.nome_jogador = novo_valor
        elif opcao == 14:
            jogador.level = novo_valor
        elif opcao == 15:
            jogador.experiencia = novo_valor
        elif opcao == 16:
            jogador.proficiencia = novo_valor
        else:
            jogador.cd = novo_valor

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
        arma = self.pega_arma_do_jogador_por_id(atacante)
        if not arma:
            return
        defensor = self.controlador_monstro.pega_monstro_por_id()
        if not defensor:
            return
        dano = 0
        if (random.randint(1,20) + atacante.proficiencia + atacante.mod_forca) > defensor.ca:
            dano += arma.dano() + atacante.mod_forca
            atacante.dano_causado.append(dano)
            defensor.dano_sofrido.append(dano)
            defensor.vida_atual -= dano
            if defensor.vida_atual <= 0:
                experiencia = (defensor.experiencia // defensor.atacado_por)
                for jogador in defensor.atacado_por:
                    jogador.recebe_experiencia(experiencia)
                self.controlador_monstro.remover_monstro(defensor)

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
            experiencia = (defensor.experiencia // defensor.atacado_por)
            for jogador in defensor.atacado_por:
                jogador.recebe_experiencia(experiencia)
            self.controlador_monstro.remover_monstro(defensor)

        dados = {
            "atacante": atacante.nome,
            "defensor": defensor.nome,
            "dano": dano
        }

        self.tela.resumo_combate(**dados)


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
            13: self.altera_atributo_da_magia,
            14: self.lanca_magia_no_monstro,
            15: self.movimentar_jogador,
            77: self.cria_jogador_teste,
        }

        super(ControladorJogador, self).mostra_tela(funcoes)

    def mapa_moveu(self, x: int, y: int):
        for i in range(len(self.__jogadores)):
            posicao = self.__jogadores[i].posicao
            self.__jogadores[i].posicao(posicao[0] - x, posicao[1] - y)

    def mostra_imagem(self, jogador):
        return jogador.imagem

    def mostra_posicao(self, jogador):
        return jogador.posicao

    def remover_jogador(self, jogador):
        self.__jogadores.remove(jogador)

    def altera_atributo_da_magia(self):
        jogador = self.pega_jogador_por_id()
        magia = self.pega_magia_por_id(jogador)
        self.controlador_magia.altera_magia(magia)

    def movimentar_jogador(self):
        jogador = self.pega_jogador_por_id()
        posicao = self.tela.movimenta_jogador()
        jogador.movimentar(posicao)
        self.controlador_principal.atualizar_visualizacao()