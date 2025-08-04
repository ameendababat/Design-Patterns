from vendingmachine import VendingMachine
from idlestate import IdleState
from hasmoneystate import HasMoneyState
from dispensingstate import DispensingState


def main():
    """Its internal state changes and the object itself dynamically switches between these state objects depending on its current state"""
    vending_machine  = VendingMachine()
    idlestate = IdleState(vending_machine)
    idlestate.insert_coin()
    hasmoneystate = HasMoneyState(vending_machine)
    hasmoneystate.eject_coin()
    dispensingstate = DispensingState(vending_machine)
    dispensingstate.finish_dispensing()
    
    
if __name__ == "__main__":
    main()