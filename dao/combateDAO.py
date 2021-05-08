from dao.dao import DAO


class CombateDAO(DAO):

    def __init__(self):
        super().__init__("combate.pkl")

    def add(self, combate: dict):
        if (combate) and (isinstance(combate["id"], int)):
            super().add(combate["id"], combate)

    def remove(self, combate: dict):
        if isinstance(combate, dict):
            super().remove(combate["id"])
    
    def get(self, id: int) -> dict:
        return super().get(id)
