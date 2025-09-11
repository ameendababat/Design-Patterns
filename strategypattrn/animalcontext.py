

class AnimalContext():
    def __init__(self, animal_strategy):
        self.animal_context = animal_strategy


    def handle_animal(self):
        self.animal_context.talk(self)
        self.animal_context.doing(self)