from paymentgateway import PaymentGateway
from stripe import Stripe


class StripeAdapter(PaymentGateway):
    def __init__(self):
        self.stripe = Stripe()


    def charge(self, amount):
        self.stripe.make_payment(amount)