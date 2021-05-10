import PySimpleGUI as sg

class TelaTamanhoInvalidoException:
    def __init__(self):
        sg.Popup('ERRO', 'Tamanho inválido, o valor deve ser um entre: Miudo, Pequeno, Medio, Grande, Enorme ou Colossal')