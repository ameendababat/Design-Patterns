from glyphfactory import GlyphFactory
from character import Character


def main():
    """Optimizes memory usage by sharing a common state among multiple objects"""
    factory = GlyphFactory()
    font = "Arial"
    size = 16
    text = "hello world"
    characters = [Character(factory.get_glyph(c, font, size),i) for i,c in enumerate(text)]
    for char in characters:
        char.render()

if __name__ == "__main__":
    main()