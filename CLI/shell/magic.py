from environment_processor import EnvironmentProcessor
from lark import Lark
from lark import Token


# грамматика строки:
# строка = list[token]
# token:
# 1. var - переменная
# 2. str - любой другой кусок строки
VAR_GRAMMAR = r"""
start: (str | var)*
str: /[^\$'\"]+/
   | /'([^'\\]?(\\')?(\\.)?)*'/
   | /\"((\\\")?(\\.)?[^\"\\]?)*\"/
var: /\$[\w_][\w\d_]*/
"""


def magic(line: str, env: EnvironmentProcessor) -> str:
    """
    Заменяет все переменные внутри строки на их значения
    :param line: строка
    :param env: процессор окружений
    :return: строка в которой все $VAL заменены на их значения или пустую строку.
    """

    # Парсим строку простой грамматикой (см выше)
    lark = Lark(VAR_GRAMMAR)
    parsed = lark.parse(line)

    # заменяем переменные на значения и собираем строку обратно
    line = ''
    for token in parsed.children:
        token_value = str(token.children[0])
        line += env.get(token_value[1:]) if token.data == 'var' else token_value

    return line