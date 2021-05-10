from limite.telaGenerica import TelaGenerica
import PySimpleGUI as sg

class TelaMagiaAlterar(TelaGenerica):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__dados_magia = {'ID': None,
                              'nome': None,
                              'quantidade_dados': None,
                              'quantidade_faces': None,
                              'circulo': None,
                              'teste': None
                              }

    def init_components(self, **kwargs):
        sg.ChangeLookAndFeel('Reddit')

        id = self.__dados_magia['ID']
        nome = self.__dados_magia['nome']
        dado = self.__dados_magia['quantidade_dados']
        faces = self.__dados_magia['quantidade_faces']
        circulo = self.__dados_magia['circulo']
        teste = self.__dados_magia['teste']

        mensagem = f'Modificar monstro: id: {id}, nome: {nome}'

        layout = [[sg.Text(mensagem, justification='center', size=(30,2))],
                  [sg.Text('Novo nome da magia:'), sg.InputText(nome, key='NOME')],
                  [sg.Text('Nova quantidade de dados:'), sg.InputText(dado, key='DADOS')],
                  [sg.Text('Nova quantidade de faces:'), sg.InputText(faces, key='FACES')],
                  [sg.Text('Novo circulo de magia'), sg.InputText(circulo, key='CIRCULO')],
                  [sg.Text('Novo teste da magia:'), sg.InputText(teste, key='TESTE')],
                  [sg.Submit('Confirmar', key='CONFIRMA'), sg.Cancel('Cancelar', key='CANCELA')]
                  ]

        janela = sg.Window('Alterar magia', default_element_size=(40, 10)).Layout(layout)
        super(TelaMagiaAlterar,self).cria_janela(janela)

    def mostra_tela(self, dados: dict):
        self.__dados_magia = dados
        return super().mostra_tela()