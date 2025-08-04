from command import Command


class DeleteTextCommand(Command):
    
    def __init__(self, document):
        self.document = document
        self.deleted = ""


    def execute(self):
        if self.document.text:
            self.deleted = self.document.text[-1]
            self.document.delete_text()


    def undo(self):
        self.document.type_text(self.deleted)