from document import Document
from commandnanager import CommandManager
from typetextcommand import TypeTextCommand
from deletetextcommand import DeleteTextCommand
from macrocommand import MacroCommand


def main():
    """Undo/Redo Functionality is Required
    """
    doc = Document()
    manager = CommandManager()
    cmd1 = TypeTextCommand(doc, "Hallo")
    manager.execute_command(cmd1)
    
    cmd2 = TypeTextCommand(doc, " word")
    manager.execute_command(cmd2)
    
    cmd3 = DeleteTextCommand(doc)
    manager.execute_command(cmd3)#Hallo wor
    
    print(doc)
    
    manager.undo()
    print("After first undo: ", doc)
    
    manager.undo()
    print("After secound undo: ", doc)


    manager.redo()
    print("After first redo: ", doc)
    
    #macro
    macro = MacroCommand()
    macro_command1 = TypeTextCommand(doc, "123")
    macro_command2 = TypeTextCommand(doc, "456")
    macro.add_command(macro_command1)
    macro.add_command(macro_command2)
    manager.execute_command(macro)
    print("After macro ", doc.text)
    manager.undo()
    print("After undo macro ", doc.text)


if __name__ == "__main__":
    main()