from limite.telaGenerica import TelaGenerica

import PySimpleGUI as sg


class TelaPersonagemRemove(TelaGenerica):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.init_components()

    def init_components(self, **kwargs):
        sg.ChangeLookAndFeel('Reddit')

        layout = [
            [sg.Text('Id do personagem para remover'), sg.InputText('', key='ID')],
            [sg.Submit('Confirmar', key='CONFIRMAR'), sg.Cancel('Cancelar', key='CANCELAR')]
        ]

        janela = sg.Window('Remove Personagem', default_element_size=(30, 10)). Layout(layout)
        super(TelaPersonagemRemove, self).cria_janela(janela)