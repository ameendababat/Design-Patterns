from handler import Handler


class RateLimitHandler(Handler):
    def handle(self, req):
        if req.get("rate") > 100:
            return False
        return super().handle(req)