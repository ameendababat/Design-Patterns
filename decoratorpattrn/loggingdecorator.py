from handlerdecorator import HandlerDecorator


class LoggingDecorator(HandlerDecorator):
    
    def handle_request(self):
        print("Logging request")
        self._handler.handle_request()