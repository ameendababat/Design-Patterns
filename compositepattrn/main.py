from rectangle import Rectangle
from group import Group


def main():
    """Dealing with a single object or a group of objects (composite) like tree data structure"""
    r1 = Rectangle()
    r2 = Rectangle()
    
    g1 = Group()
    g1.add_item(r1)
    g1.add_item(r2)
    
    g2 = Group()
    g2.add_item(g1)
    g2.add_item(r2)
    g2.draw()


if __name__ == "__main__":
    main()