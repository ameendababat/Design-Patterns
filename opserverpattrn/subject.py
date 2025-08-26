from abc import ABC, abstractmethod
from observer import Observer


class Subject(ABC):
    @abstractmethod
    def add_subscribers(self, observer:Observer):pass


    @abstractmethod
    def remove_subscribers(self, observer:Observer):pass


    @abstractmethod
    def notify_subscribers(self, user,filename):pass
    