from factorywidgets import FactoryWidgets
from button import Button
from scrollbar import ScrollBar
from menu import Menu
from windowbutton import WindowButton
from windowscrollbar import WindowScrollbar
from windowmenu import WindowMenu


class WindowsFactory(FactoryWidgets):
    
    def create_button(self)->Button:
        return WindowButton()
    
    
    def create_scrollbar(self)->ScrollBar:
        return WindowScrollbar()
    
    
    def create_menu(self)->Menu:
        return WindowMenu()
        