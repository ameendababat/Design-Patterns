from idlestate import IdleState
from hasmoneystate import HasMoneyState
from dispensingstate import DispensingState


class VendingMachine:
    
    def __init__(self):
        self.idl_state = IdleState(self)
        self.has_money_state = HasMoneyState(self)
        self.dispensing_state = DispensingState(self)
        self.state = IdleState(self)
        
        
    def set_state(self, state):
            self.state = state


    def insert_coin(self):
        self.state.insert_coin()


    def eject_coin(self):
        self.state.eject_coin()


    def select_item(self):
        self.state.select_item()


    def finish_dispensing(self):
        if isinstance(self.state, DispensingState):
            self.state.finish_dispensing()
