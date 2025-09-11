from factorywidgets import FactoryWidgets
from button import Button
from scrollbar import ScrollBar
from menu import Menu
from linuxbutton import LinuxButton
from linuxscrollbar import LinuxScrollbar


class LinuxFactory(FactoryWidgets):
    def create_button(self)->Button:
        return LinuxButton()


    def create_scrollbar(self)->ScrollBar:
        return LinuxScrollbar()


    def create_menu(self)->Menu:
        print("Menu is not supported on Linux")
        return None