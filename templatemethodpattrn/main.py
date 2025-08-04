from csvparser import CSVParser
from xmlparser import XMLParser


def  main():
    """Provides a blueprint for organizing code and making  easy to extend
        define the core steps of an algorithm in a method but allow subclasses to override specific steps
    """
    csv = CSVParser()
    csv.parser("file.csv")

    print("")
        
    xml = XMLParser()
    xml.parser("file.xml")
    
    
if __name__ == "__main__":
    main()