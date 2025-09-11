from notificationopserver import NotificationOpserver


class EmailNotifer(NotificationOpserver):
    def update(self, order):
        if order.user.email_enabled:
            print(f"[Email] send To {order.user.name}: your order {order.order_id} is now {order.status}")