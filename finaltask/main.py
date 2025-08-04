from ordersystem import OrderSystem
from user import User
from order import Order


def main():
    
    user = User('Bob')
    order = Order(1001, user)
    system = OrderSystem()
    system.place_order(order)
    system.change_status(order, "Shipped")

    system.undo()
    system.redo()

if __name__ == "__main__":
    main()