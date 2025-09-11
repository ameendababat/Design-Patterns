from notificationopserver import NotificationOpserver


class PushNotifier(NotificationOpserver):
    def update(self, order):
        if order.user.push_enabled:
            print(f"[PUSh] send To {order.user.name}: your order {order.order_id} is now {order.status}")