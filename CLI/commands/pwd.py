import os
from typing import BinaryIO
from environment_processor import EnvironmentProcessor

def pwd(stdin: BinaryIO, stdout: BinaryIO, env: EnvironmentProcessor, argv: [str]):
    """
    Выводит путь до текущей директории
    :param stdin: поток входа [не используется]
    :param stdout: поток выхода
    :param env: окружение
    :param argv: ['pwd']
    """
    if env.exit:
        return

    stdout.write('{}\n'.format(os.getcwd()).encode())


if __name__ == "__main__":
    import sys
    pwd(sys.stdin.buffer, sys.stdout.buffer, sys.argv)