from drawingmemento import DrawingMemento


class Drawing:
    """Originator """
    def __init__(self):
        self.__shapes = []
    
    
    def add_shape(self, shape):
        self.__shapes.append(shape)
    
    
    def create_memento(self):
        return DrawingMemento(self.__shapes)

    
    def restore(self, memento):
        self.__shapes = memento.shapes
    
    
    def show(self):
        print("Drawing ",self.__shapes)