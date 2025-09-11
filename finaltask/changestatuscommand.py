from command import Command

class ChangeStatusCommand(Command):
    def __init__(self, order, new_status, processor):
        self.order = order
        self.new_status = new_status
        self.processor = processor


    def execute(self):
        self.processor._internal_change_status(self.order, self.new_status)