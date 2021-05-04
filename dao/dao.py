import pickle
from abc import ABC, abstractmethod


class DAO(ABC):

    @abstractmethod
    def __init__(self, data_source=""):
        self.__data_source = "persistencia/" + data_source
        self.__cache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self.__cache, open(self.__data_source, "wb"))

    def __load(self):
        self.__cache = pickle.load(open(self.__data_source, "rb"))

    def add(self, key, object):
        self.__cache[key] = object
        self.__dump()

    def remove(self, key):
        try:
            self.__cache.pop(key)
            self.__dump()
        except KeyError:
            pass
    
    def get(self, key):
        try:
            return self.__cache[key]
        except KeyError:
            pass
    
    def get_all(self):
        return self.__cache.values()

    def get_dao(self):
        return self.__cache
