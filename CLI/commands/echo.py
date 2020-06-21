from typing import BinaryIO
from typing import List
from environment_processor import EnvironmentProcessor

def echo(stdin: BinaryIO, stdout: BinaryIO, env: EnvironmentProcessor, argv: List[str]) -> None:
    """
    Выводит аргументы через пробел
    :param stdin: Не используется
    :param stdout: Поток вывода
    :param env: окружение
    :param argv: ['echo'[, ARG1, ARG2, ...]]
    """
    if env.exit:
        return

    stdout.write(' '.join(argv[1:]).encode())
    stdout.flush()
