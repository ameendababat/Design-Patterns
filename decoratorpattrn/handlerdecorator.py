from handler import Handler


class HandlerDecorator(Handler):
    
    def __init__(self, hanler: Handler):
        self._handler = hanler


