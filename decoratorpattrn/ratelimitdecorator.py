from handlerdecorator import HandlerDecorator


class RateLimitDecorator(HandlerDecorator):
    
    def handle_request(self):
        print("Checking rate limits")
        self._handler.handle_request()