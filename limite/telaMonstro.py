from limite.telaGenerica import TelaGenerica
import PySimpleGUI as sg

class TelaMonstro(TelaGenerica):

    def __init__(self, controlador):
        super(TelaMonstro, self).__init__(controlador)
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Button('Novo monstro', key='NOVO_MONSTRO')],
            [sg.Button('Listar monstros', key='LISTA_MONSTROS')],
            [sg.Button('Excluir monstro', key='EXCLUIR_MONSTRO')],
            [sg.Button('Cadastrar ataque do monstro', key='CADASTRA_ATAQUE')],
            [sg.Button('Excluir ataque do monstro', key='EXCLUIR_ATAQUE')],
            [sg.Button('Atacar jogador', key='ATACAR_JOGADOR')],
            [sg.Button('Movimentar monstro', key='MOVIMENTAR_MONSTRO')],
            [sg.Button('Mostra atributos do monstro', key='MOSTRA_ATRIBUTOS_MONSTRO')],
            [sg.Button('Cria monstro teste', key='CRIA_MONSTRO_TESTE')],
            [sg.Button('Voltar', key='VOLTAR')]
        ]

        janela = sg.Window('Menu Monstro', default_element_size=(40,50)).Layout(layout)
        super(TelaMonstro, self).cria_janela(janela)