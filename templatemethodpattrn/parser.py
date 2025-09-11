from abc import ABC,abstractmethod


class Parser(ABC):
    """Abstruct class""" 
    def parser(self, file):
        """Template method"""
        self.load(file)
        self.validate(file)
        self.transform(file)
        self.export(file)


    def load(self, file):
        print("Load")


    def validate(self, file):pass


    def transform(self, file):
        print("Transform")


    def export(self, file):
        print("Export")