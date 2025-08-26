from animalcontext import AnimalContext
from dog import Dog
from cat import Cat
from bird import Bird
from fish import Fish
from lion import Lion


animal_dict = {
    "dog":Dog,
    "cat":Cat,
    "bird":Bird,
    "fish":Fish,
    "lion":Lion
}


if __name__ == "__main__":
    """
    Strategy pattrn and polymorphesm
    want to encapsulate the implementation details of algorithms
    Reducing Conditional Statements
    """
    while True:
        animal_name = input("Enter an animal (dog/cat/bird/fish/lion) or 'q' to quit: ").lower()
        if animal_name =="q":
            break
        animal_class = animal_dict.get(animal_name)
        if animal_class is not None:
            animal = AnimalContext(animal_class)
            animal.handle_animal()     
        else:
            print("Unknown animal.")