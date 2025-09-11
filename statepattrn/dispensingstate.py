from state import State


class DispensingState(State):
    def __init__(self, machine):
        self.machine = machine


    def insert_coin(self):
        print("Wait...dispensing item")


    def eject_coin(self):
        print("Late to eject")


    def select_item(self):
        print("Already dispensing")


    def finish_dispensing(self):
        print("Item dispensed")
        self.machine.set_state(self.machine.idl_state)