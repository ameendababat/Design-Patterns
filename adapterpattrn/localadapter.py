from paymentgateway import PaymentGateway
from local import Local


class localAdapter(PaymentGateway):
    def __init__(self):
        self.local = Local()


    def charge(self, amount):
        self.local.handle_transaction(amount)