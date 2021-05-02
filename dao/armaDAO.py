from dao.dao import DAO

from entidade.arma import Arma


class ArmaDAO(DAO):

    def __init__(self):
        super().__init__("arma.pkl")

    def add(self, arma: Arma):
        if (arma) and (isinstance(arma.id, int)):
            super().add(arma.id, arma)

    def remove(self, arma: Arma):
        if isinstance(arma, Arma):
            super().remove(arma.id)
    
    def get(self, id_arma: int) -> Arma:
        return super().get(id_arma)