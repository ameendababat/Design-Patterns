from state import State


class IdleState(State):
    
    def __init__(self, machine):
        self.machine = machine


    def insert_coin(self):
        print("Coin inserted.")
        self.machine.set_state(self.machine.has_money_state)


    def eject_coin(self):
        print("No coin to eject")


    def select_item(self):
        print("Insert coin first.")


