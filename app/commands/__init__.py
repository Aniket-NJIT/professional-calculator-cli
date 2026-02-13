from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass # pragma: no cover

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, command_name: str):
        #Easier to Ask Forgiveness than Permission
        try:
            self.commands[command_name].execute()
        except KeyError:
            print(f"No such command: {command_name}")