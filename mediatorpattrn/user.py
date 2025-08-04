

class User:
    
    def __init__(self, name):
        self.name = name
        self.chatroom = None


    def send(self, message):
        if self.chatroom:
            print(f"{self.name} sends: {message}")
            self.chatroom.broadcast(message, self)
        else:
            print(f"{self.name} is not in a chat room")


    def receive(self, message, sender):
        print(f"{self.name} received from {sender}: {message}")
        
        
    def __str__(self):
        return self.name