from limite.telaGenerica import TelaGenerica

import PySimpleGUI as sg

class TelaTeste(TelaGenerica):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')

        layout = [
                     [sg.Text("Teste:", size=(20, 2)), sg.InputText('', key='TESTE')],
                     [sg.Submit('Confirmar', key='CONFIRMAR'), sg.Cancel("Voltar", key="VOLTAR", size=(20, 2))]
                 ]

        janela = sg.Window(
            title="Menu testes",
            size=(300, 375),
            resizable=True,
            element_justification="center",
        ).Layout(layout)

        super(TelaTeste, self).cria_janela(janela)