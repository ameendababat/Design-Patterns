from paymentgateway import PaymentGateway
from paypaladapter import PaypalAdapter
from localadapter import localAdapter
from stripeadapter import StripeAdapter


def process_payment(adabter: PaymentGateway, amount):
    adabter.charge(amount)


def main():
    """
    Need to connect  components that weren’t built to work together and these incompatible interface to communicate
    """
    stripe = StripeAdapter()
    local = localAdapter()
    paypal = PaypalAdapter()
    
    process_payment(stripe, 100)
    process_payment(local, 100)
    process_payment(paypal, 100)
    
    
if __name__ == "__main__":
        main()