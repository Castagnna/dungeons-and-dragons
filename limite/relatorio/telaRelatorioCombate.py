# Limites
from limite.telaGenerica2 import TelaGenerica

# Utils
from PySimpleGUI import PySimpleGUI as sg


class TelaRelatorioCombate(TelaGenerica):

    def __init__(self, controlador):
        super().__init__(controlador)
        self.__combates = []
        self.init_components()

    @staticmethod
    def monta_lista_str(combates: list):

        def monta_string(id, atacante, defensor, dano):
            return f"{id:^4}|{atacante:^10}|{defensor:^9}|{dano:^6}"

        lista_str = ["evento | atacante | defensor | dano"]
        
        for combate in combates:
            string = monta_string(
                combate["id"],
                combate["atacante"].nome,
                combate["defensor"].nome,
                combate["dano"],
            )
            lista_str.append(string)

        return lista_str

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')

        valores = self.monta_lista_str(self.__combates)

        layout = [
            [sg.Listbox(values=valores, size=(30, 6))],
            [sg.Cancel("OK", key="OK")],
        ]

        janela = sg.Window("Eventos de combate", default_element_size=(40, 10)).Layout(layout)
        super(TelaRelatorioCombate, self).cria_janela(janela)

    def mostra_tela(self, combates: list):
        self.__combates = combates
        return super().mostra_tela()
