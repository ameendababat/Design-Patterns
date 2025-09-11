import copy 
from prototype import Prototype


class NPC(Prototype):
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon


    def clone(self):
        return copy.deepcopy(self)


    def __str__(self):
        return f"NPC: name: {self.name} weapon: {self.weapon} "    