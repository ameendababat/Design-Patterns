from factorywidgets import FactoryWidgets
from button import Button
from scrollbar import ScrollBar
from menu import Menu
from macbutton import MacButton
from macscrollbar import MacScrollbar
from macmenu import MacMenu


class MacFactory(FactoryWidgets):
    def create_button(self)->Button:
        return MacButton()


    def create_scrollbar(self)->ScrollBar:
        return MacScrollbar()


    def create_menu(self)->Menu:
        return MacMenu()