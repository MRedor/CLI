from typing import BinaryIO, Dict
from environment_processor import EnvironmentProcessor


def wc(stdin: BinaryIO, stdout: BinaryIO, env: EnvironmentProcessor, argv: [str]) -> None:
    """
    Моделирует работу wc
    :param stdin: поток ввода. используется если argv не содержит имя файла.
    :param stdout: поток вывода.
    :param env: окружение
    :param argv: ['wc', [FILE]]
    """
    if env.exit:
        return

    need_to_close = False
    if len(argv) > 1:
        need_to_close = True
        stdin = open(argv[1], 'rb')

    bytes_count = 0
    words_count = 0
    lines_count = 0
    for line in stdin:
        lines_count += 0 if line.count(b'\n') == 0 else 1
        bytes_count += len(line)
        words_count += len(line.split())

    stdout.write("    {lines}    {words}    {bytes}\n".format(
        lines=lines_count, words=words_count, bytes=bytes_count).encode())

    if need_to_close:
        stdin.close()
