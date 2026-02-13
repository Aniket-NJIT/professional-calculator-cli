"""
Commands module.
Implements the Command Pattern for handling REPL operations.
"""
from abc import ABC, abstractmethod

class Command(ABC):
    """
    Abstract base class for all commands.
    """
    @abstractmethod
    def execute(self):
        """
        Executes the command.
        """
        pass  # pragma: no cover

class CommandHandler:
    """
    Handles registration and execution of commands.
    """
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        """
        Registers a command with a name.
        """
        self.commands[command_name] = command

    def execute_command(self, command_name: str):
        """
        Executes a registered command by name.
        """
        # EAFP: Easier to Ask Forgiveness than Permission
        try:
            self.commands[command_name].execute()
        except KeyError:
            print(f"No such command: {command_name}")