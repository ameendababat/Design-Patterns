from handlerdecorator import HandlerDecorator


class AuthDecorator(HandlerDecorator):
    def handle_request(self):
        print("Validating auth")
        self._handler.handle_request()