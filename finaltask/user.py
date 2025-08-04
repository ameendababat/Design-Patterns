

class User:
    
    def __init__(self, name):
        self.name = name
        self.email_enabled = True
        self.sms_enabled = False
        self.push_enabled = True