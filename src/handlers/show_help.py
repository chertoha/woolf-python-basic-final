from typing import List
from src.decorators.catch import catch
from src.cli.commands import commands


@catch
def show_help(args: List[str]):
    print("Available commands:")
    for command, details in commands.items():
        description = details.get("description", "No description available")
        print(f"- {command.value}: {description}")