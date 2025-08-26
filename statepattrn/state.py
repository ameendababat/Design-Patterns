from abc import ABC, abstractmethod


class State(ABC):
    @abstractmethod
    def insert_coin(self):pass


    @abstractmethod
    def eject_coin(self):pass


    @abstractmethod
    def select_item(self):pass