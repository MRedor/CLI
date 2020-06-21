import typing
from environment_processor import EnvironmentProcessor

def exit_command(stdin: typing.BinaryIO, stdout: typing.BinaryIO, env: EnvironmentProcessor, argv: [str]) -> None:
    """
    выставляем env.exit = True
    :param stdin: [не используется]
    :param stdout: [не используется]
    :param env: окружение
    :param argv: [exit]
    """
    env.exit = True
    return

if __name__ == "__main__":
    import sys
    exit_command(sys.stdin.buffer, sys.stdout.buffer, sys.argv)
