import argparse
import re

from typing import BinaryIO
from environment_processor import EnvironmentProcessor


class ArgumentParserError(Exception):
    pass


class ThrowingArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        raise ArgumentParserError(message)


def parse_arguments(args: [str]):
    parser = ThrowingArgumentParser()
    parser.add_argument('-i', default=False, action='store_true')
    parser.add_argument('-w', default=False, action='store_true')
    parser.add_argument('-A', default=0, type=int)
    parser.add_argument('pattern', type=str)
    parser.add_argument('file', type=str, nargs='?')
    return parser.parse_args(args)


def check_line(line: str, pattern: str, i: bool, w:bool) -> bool:
    """
    Проверяем подходит ли данная строка под параметры поиска
    :param line: строка
    :param pattern: шаблон
    :param i: флаг учета регисра
    :param w: флаг слова целиком
    :return: True - подходит, False - нет
    """
    parts = [line] if not w else re.split(r'[^\w\d_]+', line)
    find_func = re.match if w else re.search
    for part in parts:
        march = find_func(pattern, part, re.IGNORECASE) if i else find_func(pattern, part)
        if march and (not w or str(march.group(0)) == part):
            return True
    return False


def grep(stdin: BinaryIO, stdout: BinaryIO, env: EnvironmentProcessor, argv: [str]) -> None:
    """
    Ишет паттерн среди строк stdin или файла если он задан
    :param stdin: входной поток
    :param stdout: выходной поток
    :param env: окружение
    :param argv: аргументы командной строки
    """
    if env.exit:
        return

    try:
        args = parse_arguments(argv[1:])
    except ArgumentParserError as ex:
        stdout.write(b'ERROR:' + str(ex).encode() + b'\n')
        return

    if args.A < 0:
        stdout.write(b'-A VAL: VAL must be positive\n')
        return

    need_to_close = False
    if args.file:
        need_to_close = True
        stdin = open(args.file, 'rb')

    data = stdin.readlines()
    line_indexes = set()
    for index, line in enumerate(data):
        if check_line(line.decode(), args.pattern, args.i, args.w):
            line_indexes.add(index)
            for additional in range(args.A + 1):
                line_indexes.add(index + additional)

    for index, line in enumerate(data):
        if index in line_indexes:
            stdout.write(line)

    if need_to_close:
        stdin.close()


if __name__ == "__main__":
    import sys
    grep(sys.stdin.buffer, sys.stdout.buffer, EnvironmentProcessor(), ['grep', '-w', '-A', '3', 'parser', 'grep.py'])

