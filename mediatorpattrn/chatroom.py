

class ChatRoom:
    """Mediator"""
    def __init__(self):
        self.users = []

    
    def register(self, user):
        
        self.users.append(user)
        user.chatroom = self
        


    def broadcast(self, message, sender):
        for user in self.users:
            if user != sender:
                user.receive(message, sender)