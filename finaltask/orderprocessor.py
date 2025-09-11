from loggerstrategy import LoggerStrategy
from ordercaretaker import OrderCaretaker
from notificationopserver import NotificationOpserver
import time


class OrderProcessor:
    """Subject opserver"""
    def __init__(self, logger:LoggerStrategy):
        self.opservers = []
        self.logger = logger
        self.caretaker = OrderCaretaker()
    
    
    def add_opserver(self, observer:NotificationOpserver):
        self.opservers.append(observer)


    def notify(self, order):
        for ops in self.opservers:
            ops.update(order)
    
    
    def _internal_process_order(self, order):
        self.logger.log(f"Processing order {order.order_id} for user name: {order.user.name}")
        time.sleep(1)
        order.status = "processed"
        self.logger.log(f"Order {order.order_id} Processed")
        self.notify(order)


    def _internal_change_status(self, order, new_status):
        self.caretaker.save(order)
        order.status = new_status
        self.logger.log(f"Order {order.order_id} status changed to {new_status}")
        self.notify(order)


    def undo_status(self):
        self.caretaker.undo()


    def redo_status(self):
        self.caretaker.redo()