from copy import deepcopy


class DrawingMemento:
    """Memento"""
    def __init__(self, shapes_snapshot):
        self.__shapes = tuple(deepcopy(shapes_snapshot))#Immutable snapshot
    
    
    @property
    def shapes(self):
        return list(self.__shapes)