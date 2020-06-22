from environment_processor import EnvironmentProcessor

from lark import Lark
from lark.tree import Tree
from typing import Union

from shell.magic import magic_light

LINE_GRAMMAR = r"""
start: line | empty

line: simple
    | pipe

pipe: simple " "* "|" " "* line

simple: declaration
      | command

declaration: str "=" str
command: str (" "+ str)*

str: (word | lq | sq)+

word: /[^\s|\"';=]+/
lq: /\"((\\\")?(\\.)?[^\"\\]?)*\"/
sq: /'([^'\\]?(\\.)?(\\')?)*'/

empty: /\s+/
"""


def parse_string(line):
    lark = Lark(LINE_GRAMMAR)
    return lark.parse(line)


def parse_shell_line(line: str, env: EnvironmentProcessor) -> Union[Tree, Tree]:
    # парсим переменные и заменяем их значениями.
    line_without_vars = magic_light(line, env)
    # строим дерево
    return parse_string(line_without_vars)


if __name__ == "__main__":
    print(parse_shell_line("wc shell.py", EnvironmentProcessor()))
    print(parse_shell_line("echo ko", EnvironmentProcessor()))
    print(parse_shell_line("wc shell.py $PATH", EnvironmentProcessor()))