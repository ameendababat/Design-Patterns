from glyph import Glyph


class GlyphFactory:
    def __init__(self):
        self.__glyphs = {}


    def get_glyph(self, char, font, size):
        key = (char, font, size)
        if key not in self.__glyphs:
            self.__glyphs[key] = Glyph(char, font , size)
        return self.__glyphs[key]    