from command import Command


class MacroCommand(Command):
    def __init__(self):
        self.commands = []


    def add_command(self, cmd):
        self.commands.append(cmd)


    def execute(self):
        for cmd in self.commands:
            cmd.execute()


    def undo(self):
        for cmd in reversed(self.commands):
            cmd.undo()