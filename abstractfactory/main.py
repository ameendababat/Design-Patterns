from windowfactory import WindowsFactory
from macfactory import MacFactory
from linuxfactory import LinuxFactory


def draw_ui(factory):
    button = factory.create_button()
    scrollbar = factory.create_scrollbar()
    menu = factory.create_menu()
    if button and scrollbar and menu:
        button.draw()
        scrollbar.draw()
        menu.draw()


def main():
    """
    System requires multiple families of related os -- objects
    """
    factory = WindowsFactory()
    draw_ui(factory)


if __name__ == "__main__":
    main()