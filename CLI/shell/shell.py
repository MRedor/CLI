from environment_processor import EnvironmentProcessor

from shell.parser import parse_shell_line
from shell.runner import run

from io import StringIO, BytesIO


class Shell:
    def __init__(self, stdin=StringIO(), stdout=StringIO()):
        self.env = EnvironmentProcessor()
        self.stdin = stdin
        self.stdout = stdout

    def __process_line(self, line: str) -> None:
        """
        Парсится и выполняется строка
        :param line:  строка
        """
        if line == '':
            return
        try:
            stdin = BytesIO()
            stdout = BytesIO()
            expr = parse_shell_line(line, self.env)
            run(expr, stdin, stdout, self.env)
            self.stdout.write(stdout.getvalue().decode())
        except Exception as exception:
            self.stdout.write(str(exception))
        self.stdout.flush()

    def start(self) -> None:
        """
        запускает шел. шел живет пока на вход не подадут команду exit.
        :return:
        """
        while not self.env.exit:
            line = self.stdin.readline().rstrip()
            self.__process_line(line)
