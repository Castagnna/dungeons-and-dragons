from limite.telaGenerica import TelaGenerica
import PySimpleGUI as sg


class TelaJogador(TelaGenerica):
    def __init__(self, controlador):
        super(TelaJogador, self).__init__(controlador)
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Button('Novo jogador', key='NOVO_JOGADOR')],
            [sg.Button('Mostra jogadores', key='MOSTRA_JOGADORES')],
            [sg.Button('Remover jogador', key='REMOVE_JOGADOR')],
            [sg.Button('Mostrar atributos do jogador', key='ATRIBUTOS_JOGADOR')],
            [sg.Button('Alterar atributos do jogador', key='ALTERA_ATRIBUTOS_JOGADOR')],
            [sg.Button('Equipar arma', key='EQUIPA_ARMA')],
            [sg.Button('Desequipar arma', key='DESEQUIPA_ARMA')],
            [sg.Button('Mostrar armas do jogador', key='MOSTRA_ARMAS')],
            [sg.Button('Atacar monstro', key='ATACA_MONSTRO')],
            [sg.Button('Vincular magia', key='VINCULA_MAGIA')],
            [sg.Button('Desvincular magia', key='VINCULA_MAGIA')],
            [sg.Button('Mostrar magias do jogador', key='MOSTRA_MAGIAS')],
            [sg.Button('Alterar atributos de magia', key='ALTERA_ATRIBUTOS_MAGIA')],
            [sg.Button('Lancar magia no monstro', key='LANCA_MAGIA')],
            [sg.Button('Movimentar jogador', key='MOVIMENTAR_JOGADOR')],
            [sg.Button('Criar jogador teste', key='CRIA_JOGADOR_TESTE')],
            [sg.Button('Voltar', key='VOLTAR')]
        ]

        janela = sg.Window('Menu Jogador', default_element_size=(40,50)).Layout(layout)
        super(TelaJogador, self).cria_janela(janela)