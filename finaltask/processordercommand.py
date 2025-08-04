from command import Command

class ProcessOrderCommand(Command):
    
    def __init__(self, order, processor):
        self.order = order
        self.processor = processor
    
    
    def execute(self):
        self.processor._internal_process_order(self.order)