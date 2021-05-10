from dao.dao import DAO
from entidade.background import Background

class BackgroundDAO(DAO):
    def __init__(self):
        super().__init__('background.pkl')
