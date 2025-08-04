


class Character:
    
    def __init__(self, glyph, pos):
        self.glyph = glyph
        self.pos = pos
    
    
    def render(self):
        self.glyph.render(self.pos)