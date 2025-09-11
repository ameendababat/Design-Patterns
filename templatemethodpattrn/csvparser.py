from parser import Parser


class CSVParser(Parser):
    def validate(self, file):
        print("ValidateCSV")