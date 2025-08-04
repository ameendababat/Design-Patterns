from abc import ABC, abstractmethod
from report import Report 


class Builder(ABC):
    
    @abstractmethod
    def title(self, title):pass
    
    
    @abstractmethod
    def toc(self, toc=True):pass
    
    
    @abstractmethod
    def data(self, data=True):pass
    
    
    @abstractmethod
    def chart(self, chart=True):pass
    
    
    @abstractmethod
    def appendx(self, appendx=True):pass
    
    
    @abstractmethod
    def build(self)->Report:pass
    