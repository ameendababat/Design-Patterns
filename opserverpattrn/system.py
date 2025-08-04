from subject import Subject
from observer import Observer


class System(Subject):
    
    def __init__(self):
        self.__observers = []
    
    
    def add_subscribers(self, observer:Observer):
        self.__observers.append(observer)


    def remove_subscribers(self, observer:Observer):
        self.__observers.remove(observer)


    def notify_subscribers(self, user, filename):
        for observer in self.__observers:
            observer.update(user, filename)
