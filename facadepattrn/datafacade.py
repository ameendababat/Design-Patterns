from cache import Cache
from db import DB
from api import API


class DataFacade:
    """Facade pattrn"""
    def __init__(self):
        self.__cache = Cache()
        self.__db = DB()
        self.__api = API()


    def get_cache(self, key):
        self.__cache.get(key)


    def get_db(self, table):
        self.__db.fetch(table)


    def get_api(self):
        self.__api.call()