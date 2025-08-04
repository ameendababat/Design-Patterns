from chatroom import ChatRoom
from user import User


def main():
    """Complex communication and loose coupling between objects allowing them 
        to interact without knowing the details of each other's implementations"""
    chatroom = ChatRoom()
    user1 = User("Alice")
    user2 = User("ameen")
    chatroom.register(user1)
    chatroom.register(user2)
    user1.send("hi iam alice")
    user2.send("hi iam ameen")
    
if __name__ == "__main__":
    main()