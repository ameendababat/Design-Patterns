from ordermemento import OrderMemento


class OrderCaretaker:
    
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []


    def save(self, order):
        self.undo_stack.append((order,OrderMemento(order.status)))
        self.redo_stack.clear()
    
    
    def undo(self):
        if not self.undo_stack:
            print("Nothing to undo")
            return
        order, memento = self.undo_stack.pop()
        self.redo_stack.append((order, OrderMemento(order.status)))
        order.status = memento.status
        print(f"Undo: order: {order.order_id} status changed to {order.status}")


    def redo(self):
        if not self.redo_stack:
            print("Nothing to redo")
            return
        order, memento = self.redo_stack.pop()
        self.undo_stack.append((order, OrderMemento(order.status)))
        order.status = memento.status
        print(f"Redo: order: {order.order_id} status changed to {order.status}")