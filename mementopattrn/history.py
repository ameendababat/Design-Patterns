

class History:
    """Caretaker """
    def __init__(self):
        self.__mementos = []
    
    
    def save(self, memento):
        self.__mementos.append(memento)
    
    
    def undo(self):
        if self.__mementos:
            return self.__mementos.pop()
        else:
            return None