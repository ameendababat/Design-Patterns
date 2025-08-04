from handler import Handler

class AuthHandler(Handler):
    
    def handle(self, req):
        if not req.get("auth"):
            return False
        return super().handle(req)