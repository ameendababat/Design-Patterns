from handler import Handler


class VirusScanHandler(Handler):
    def handle(self, req):
        if "virus" in req.get("content"):
            return False
        return super().handle(req)