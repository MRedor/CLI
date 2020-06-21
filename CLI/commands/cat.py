from typing import BinaryIO
from environment_processor import EnvironmentProcessor

def cat(stdin: BinaryIO, stdout: BinaryIO, env: EnvironmentProcessor, argv: [str]) -> None:
    """
    Печает содержимое файла или входного потока
    :param stdin: Входной поток. Используется если имя файла не задано.
    :param stdout: Выходной поток.
    :param env: окружение
    :param argv: ['cat', [FILE]]
    """
    if env.exit:
        return

    need_to_close = False
    if len(argv) > 1:
        need_to_close = True
        stdin = open(argv[1], 'rb')

    stdout.write(stdin.read())

    if need_to_close:
        stdin.close()
