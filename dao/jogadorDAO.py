from dao.dao import DAO

from entidade.jogador import Jogador


class JogadorDAO(DAO):

    def __init__(self):
        super().__init__("jogador.pkl")

    def add(self, jogador: Jogador):
        if (jogador) and (isinstance(jogador.id, int)):
            super().add(jogador.id, jogador)

    def remove(self, jogador: Jogador):
        if isinstance(jogador, Jogador):
            super().remove(jogador.id)
    
    def get(self, id: int) -> Jogador:
        return super().get(id)