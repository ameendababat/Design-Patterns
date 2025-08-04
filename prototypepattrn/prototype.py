from abc import ABC,abstractmethod
import copy 


class Prototype(ABC):
    
    @abstractmethod
    def clone(self):pass