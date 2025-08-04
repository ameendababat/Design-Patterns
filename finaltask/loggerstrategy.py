from abc import ABC, abstractmethod


class LoggerStrategy(ABC):
    
    @abstractmethod
    def log(self, message):pass