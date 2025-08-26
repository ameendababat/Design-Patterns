

class Order:
    def __init__(self, order_id, user):
        self.order_id = order_id
        self.user = user 
        self.status = "Created"