from dao.dao import DAO

from entidade.monstro import Monstro


class MonstroDAO(DAO):

    def __init__(self):
        super().__init__("monstro.pkl")

    def add(self, monstro: Monstro):
        if (monstro) and (isinstance(monstro.id, int)):
            super().add(monstro.id, monstro)

    def remove(self, monstro: Monstro):
        if isinstance(monstro, Monstro):
            super().remove(monstro.id)
    
    def get(self, id: int) -> Monstro:
        return super().get(id)