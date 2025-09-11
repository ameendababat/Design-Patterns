

class Glyph:
    """Flyweight class"""
    def __init__(self, char, font, size):#intrinsic data shared 
        self.char = char
        self.font = font
        self.size = size


    def render(self, pos):#extrinsic data unique 
        self.pos = pos
        print(f"{self.char} at {self.pos} font: {self.font} size: {self.size}px")