from abc import ABC,abstractmethod
from button import Button
from scrollbar import ScrollBar
from menu import Menu

class FactoryWidgets(ABC):
    
    @abstractmethod
    def create_button(self)->Button:pass
    
    
    @abstractmethod
    def create_scrollbar(self)->ScrollBar:pass
    
    @abstractmethod
    def create_menu(self)->Menu:pass
    