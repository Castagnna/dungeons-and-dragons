# Limites
from limite.telaGenerica import TelaGenerica

# Utils
from PySimpleGUI import PySimpleGUI as sg


class TelaAtaqueNovo(TelaGenerica):

    def __init__(self, controlador):
        super().__init__(controlador)
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')

        testes = [
            "Forca", "Destreza", "Constituicao", 
            "Sabedoria", "Inteligencia", "Carisma", "Nenhum"
        ]

        layout = [
            [sg.Text("Nome do ataque:"), sg.InputText("", key="NOME")],
            [sg.Text("Quantidade de dados:"), sg.Slider(range=(1, 10), orientation='h', size=(10, 20), default_value=1, key="DADOS")],
            [sg.Text("Numero de faces:"), sg.Slider(range=(1, 20), orientation='h', size=(10, 20), default_value=1, key="FACES")],
            [sg.Text("Dano bonus:"), sg.Slider(range=(1, 20), orientation='h', size=(10, 20), default_value=1, key="BONUS")],
            [sg.Text("Acerto:"), sg.Slider(range=(1, 20), orientation='h', size=(10, 20), default_value=1, key="ACERTO")],
            [sg.Text("CD:"), sg.Slider(range=(1, 20), orientation='h', size=(10, 20), default_value=1, key="CD")],
            [
                sg.Text('Teste: ', size=(6, 1), auto_size_text=False, justification='right'),
                sg.InputCombo(testes, size=(14, 1), default_value="Nenhum", key="TESTE"),
            ],
            [sg.Submit("Confirmar", key="CONFIRMAR"), sg.Cancel("Cancelar", key="CANCELAR")],
        ],

        janela = sg.Window("Novo ataque monstro", default_element_size=(40, 10)).Layout(layout)
        super(TelaAtaqueNovo, self).cria_janela(janela)
