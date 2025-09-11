from paymentgateway import PaymentGateway
from paypal import PayPal


class PaypalAdapter(PaymentGateway):
    def __init__(self):
        self.paypal = PayPal()


    def charge(self, amount):
        self.paypal.send_payment(amount)