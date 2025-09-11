from infologger import InfoLogger
from orderprocessor import OrderProcessor
from emailnotifer import EmailNotifer
from smsnotifier import SMSNotifier
from pushnotifier import PushNotifier
from processordercommand import ProcessOrderCommand
from changestatuscommand import ChangeStatusCommand


class OrderSystem:
    """Facade Pattern - clint"""
    def __init__(self):
        self.logger = InfoLogger()
        self.processor = OrderProcessor(self.logger)
        self.processor.add_opserver(EmailNotifer())
        self.processor.add_opserver(SMSNotifier())
        self.processor.add_opserver(PushNotifier())


    def place_order(self, order):
        cmd = ProcessOrderCommand(order, self.processor)
        cmd.execute()


    def change_status(self, order, new_status):
        cmd = ChangeStatusCommand(order, new_status, self.processor)
        cmd.execute()


    def undo(self):
        self.processor.undo_status()


    def redo(self):
        self.processor.redo_status()