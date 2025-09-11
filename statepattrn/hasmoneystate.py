from state import State


class HasMoneyState(State):
    def __init__(self, machine):
        self.machine = machine


    def insert_coin(self):
        print("Already has money")
        self.machine.set_state(self.machine.has_money_state)


    def eject_coin(self):
        print("Coin ejected.")
        self.machine.set_state(self.machine.idl_state)


    def select_item(self):
        print("Item selected")
        self.machine.set_state(self.machine.dispensing_state)


    