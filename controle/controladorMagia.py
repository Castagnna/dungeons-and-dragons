from limite.telaMagia import TelaMagia
from limite.telaMagiaAlterar import TelaMagiaAlterar
from limite.telaMagiaNova import TelaMagiaNova
from limite.telaMagiaPega import TelaMagiaPega
from limite.telaTeste import TelaTeste

from excecao.testeInvalidoException import TesteInvalidoException



from entidade.magia import Magia


class ControladorMagia:
    def __init__(self, controlador_jogador):
        self.__tela = TelaMagia(self)
        self.__tela_alterar = TelaMagiaAlterar(self)
        self.__tela_nova = TelaMagiaNova(self)
        self.__tela_pega = TelaMagiaPega(self)
        self.__tela_teste = TelaTeste(self)
        self.__controlador_jogador = controlador_jogador
        self.__counta_magias = 0

    @property
    def controlador(self):
        return self.__controlador_jogador

    def cria_magia(self, evento='CONFIRMAR', valores: dict=None) -> Magia:
        testes_validos = ['FORCA', 'DESTREZA', 'CONSTITUICAO', 'INTELIGENCIA', 'SABEDORIA', 'CARISMA']
        if not valores:
            evento, valores = self.__tela_nova.mostra_tela()

        if evento == 'CONFIRMAR':
            while True:
                try:
                    if valores['NOME'] == '':
                        break
                    elif valores['TESTE'].upper() not in testes_validos:
                        raise TesteInvalidoException
                    else:
                        magia = Magia(id=self.__counta_magias,
                                    nome=valores['NOME'],
                                    quantidade_dado=int(valores['DADOS']),
                                    numero_faces=int(valores['FACES']),
                                    circulo=int(valores['CIRCULO']),
                                    teste=valores['TESTE'])
                        self.__counta_magias += 1
                        self.__tela_nova.fecha_tela()
                        return magia
                except TesteInvalidoException:
                    self.__tela_nova.fecha_tela()
                    evento, valor = self.__tela_teste.mostra_tela()
                    self.__tela_teste.fecha_tela()
                    valores['TESTE'] = valor['TESTE']
                    if evento != 'CONFIRMAR':
                        break

        self.__tela_nova.popup_falha()
        self.__tela_nova.fecha_tela()

    def pega_magia_por_id(self):
        lista_ordenada_de_magias = self.ordena_valores_do_dicionario_pela_chave()

        mostra_tela = True

        while mostra_tela:
            evento, valores = self.__tela_pega.mostra_tela(lista_ordenada_de_magias)

            if evento  == 'CONFIRMA':
                try:
                    id = int(valores['ID'])
                    mostra_tela = False
                    self.__tela_pega.fecha_tela()
                    return #magia
                except ValueError:
                    self.__tela_pega.popup_falha(mensagem='O valor precisa ser inteiro')
                    self.__tela_pega.fecha_tela()
                except KeyError:
                    self.__tela_pega.popup_falha(mensagem='Magia nao encontrada')
                    self.__tela_pega.fecha_tela()
            elif evento == 'CANCELA' or evento == None:
                mostra_tela = False
                self.__tela_pega.fecha_tela()
        return None

    def ordena_valores_do_dicionario_pela_chave(self, dicionario: dict):
        lista_ordenada = []
        for key in sorted(dicionario.keys()):
            lista_ordenada.append(dicionario[key])
        return lista_ordenada

    def mostra_tela(self):
        evento, _ = self.__tela.mostra_tela()

        if evento == 'VOLTAR':
            self.__tela.fecha_tela()
            self.__controlador_jogador.mostra_tela()

        funcoes = {
            'NOVA_MAGIA': self.cria_magia,
            'ALTERA_MAGIA': self.altera_magia
        }
        try:
            self.__tela.fecha_tela()
            funcoes[evento]()
            self.mostra_tela()
        except KeyError:
            pass

    def altera_magia(self, magia):

        if not isinstance(magia, Magia):
            self.__tela_alterar.fecha_tela()

        dados = {
            'ID': magia.id,
            'NOME': magia.nome,
            'DADOS': magia.quantidade_dado,
            'FACES': magia.numero_faces,
            'CIRCULO': magia.circulo,
            'TESTE': magia.teste
        }

        evento, valores = self.__tela_alterar.mostra_tela(dados)

        if evento == 'CONFIRMA':
            magia.nome = valores['NOME']
            magia.quantidade_dado = valores['DADOS']
            magia.numero_faces = valores['FACES']
            magia.circulo = valores['CIRCULO']
            magia.teste = valores['TESTE']