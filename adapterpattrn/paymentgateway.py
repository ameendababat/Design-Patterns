from abc import ABC,abstractmethod

class PaymentGateway(ABC):
    
    @abstractmethod
    def charge(self, amount):pass