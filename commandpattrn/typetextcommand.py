from command import Command


class TypeTextCommand(Command):
    def __init__(self, document, text):
        self.document = document
        self.text = text


    def execute(self):
        self.document.type_text(self.text)


    def undo(self):
        self.document.text = self.document.text[:-len(self.text)]