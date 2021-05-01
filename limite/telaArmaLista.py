# Models
from entidade.arma import Arma

# Views
from limite.telaGenerica import GeneralScreen

# Controllers
# from controle.controladorArma import ControladorArma

# Utils
from PySimpleGUI import PySimpleGUI as sg


class TelaArmaLista(GeneralScreen):

    def __init__(self, controlador):
        super().__init__(controlador)
        self.__janela = None
        self.__lista_de_armas = None
        self.init_components()

    def monta_lista(self):

        def monta_string(id, nome, dados, faces):
            return " ; ".join([str(id), str(nome), str(dados), str(faces)])
        
        lista_de_armas = ["0 ; teste ; 2 ; 4"]

        for id in sorted(self.controlador.armas.keys()):
            arma = self.controlador.armas[id]
            string = monta_string(
                arma.id,
                arma.nome,
                arma.quantidade_dado,
                arma.numero_faces,
            )
            lista_de_armas.append(string)
            lista_de_armas.append("2 ; teste ; 3 ; 5")
            
        lista_de_armas.append("3 ; teste ; 3 ; 5")

        return lista_de_armas

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')

        valores = self.monta_lista()

        layout = [
            [sg.Text('Id ; Nome ; Dados ; Faces', background_color='#d3dfda', justification='center', size=(30, 2))],
            [sg.Listbox(values=valores, size=(30, 6))],
            [sg.Cancel("OK", key="OK")],
        ]

        self.__janela = sg.Window("Lista de armas", default_element_size=(40, 10)).Layout(layout)

    def mostra_tela(self, lista_de_armas: list=[]):
        self.__lista_de_armas = lista_de_armas
        return self.__janela.Read()

    def fecha_tela(self):
        self.__janela.Close()