from drawing import Drawing
from history import History


def  main():
    """Save and restore an object's state without exposing its internal details and Undo functionality"""
    drawing = Drawing()
    history = History()
    
    drawing.add_shape("Circle")
    history.save(drawing.create_memento())
    drawing.add_shape("Square")
    history.save(drawing.create_memento())
    drawing.show()
    
    drawing.add_shape("Triangle")
    
    drawing.show()
    
    drawing.restore(history.undo())
    drawing.show()
    
    drawing.restore(history.undo())
    drawing.show()

if __name__ == "__main__":
    main()