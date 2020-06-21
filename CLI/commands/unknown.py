from typing import BinaryIO
from environment_processor import EnvironmentProcessor

import subprocess


def unknown(stdin: BinaryIO, stdout: BinaryIO, env: EnvironmentProcessor, argv: [str]) -> None:
    """
    Запускает команду argv[0] через subprocess
    :param stdin: поток входа
    :param stdout: поток выхода
    :param env: окружение
    :param argv: аргументы для запуска [command, [args]]
    """
    if env.exit:
        return

    sp = subprocess.Popen(argv, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    sp.stdin.write(stdin.read())
    output, _ = sp.communicate()
    stdout.write(output)

