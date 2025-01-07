from src.cli.commands import execute_command
from src.cli.parser import parse_input


def app() -> None:

    while True:
        try:
            user_input = input("Enter a command: ").strip()
            command, *args = parse_input(user_input)

            if command in ["exit", "quit", "end"]:
                print("Bye!")
                break

            execute_command(command, args)

        except Exception as err:
            print(err)
