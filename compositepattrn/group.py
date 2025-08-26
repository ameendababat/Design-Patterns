from shape import Shape


class Group:
    """Composite"""
    def __init__(self):
        self.items = []


    def add_item(self, shape):
        self.items.append(shape)


    def draw(self):
        for item in self.items:
            item.draw()