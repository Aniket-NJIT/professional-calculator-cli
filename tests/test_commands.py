import pytest
from app.commands import CommandHandler, Command

class MockCommand(Command):
    def __init__(self):
        self.executed = False
    def execute(self):
        self.executed = True

def test_register_and_execute_command():
    handler = CommandHandler()
    mock_cmd = MockCommand()
    handler.register_command("test", mock_cmd)
    handler.execute_command("test")
    assert mock_cmd.executed is True

def test_execute_invalid_command(capsys):
    """Test that invalid command prints error (EAFP verification)."""
    handler = CommandHandler()
    handler.execute_command("invalid")
    captured = capsys.readouterr()
    assert "No such command: invalid" in captured.out