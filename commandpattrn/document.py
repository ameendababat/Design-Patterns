

class Document:
    """Receiver """
    def __init__(self):
        self.text = ""


    def type_text(self, content):
        self.text += content


    def delete_text(self, doc=1):
        if self.text:
            self.text = self.text[:-doc]


    def __str__(self):
        return self.text