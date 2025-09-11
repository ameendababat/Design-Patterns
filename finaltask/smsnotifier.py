from notificationopserver import NotificationOpserver


class SMSNotifier(NotificationOpserver):
    def update(self, order):
        if order.user.sms_enabled:
            print(f"[SMS] send To {order.user.name}: your order {order.order_id} is now {order.status}")