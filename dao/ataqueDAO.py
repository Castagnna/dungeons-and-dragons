from dao.dao import DAO

from entidade.ataqueMonstro import AtaqueMonstro


class AtaqueDAO(DAO):

    def __init__(self):
        super().__init__("ataque_monstro.pkl")

    def add(self, ataque: AtaqueMonstro):
        if (ataque) and (isinstance(ataque.id, int)):
            super().add(ataque.id, ataque)

    def remove(self, ataque: AtaqueMonstro):
        if isinstance(ataque, AtaqueMonstro):
            super().remove(ataque.id)
    
    def get(self, id: int) -> AtaqueMonstro:
        return super().get(id)