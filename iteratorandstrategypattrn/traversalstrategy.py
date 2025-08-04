from abc import ABC,abstractmethod


class TraversalStrategy(ABC):
    
    @abstractmethod
    def create_iterator(self, items):pass