from environment_processor import EnvironmentProcessor
from lark import Lark


# грамматика строки:
# строка = list[token]
# token:
# 1. var - переменная
# 2. str - любой другой кусок строки
VAR_GRAMMAR_LIGHT = r"""
start: (str | var)*
str: /[^\$'\"]+/
   | /'([^'\\]?(\\')?(\\\.)?)*'/
   | /\"([^\"\\]?(\\\")?(\\\.)?)*\"/
var: /\$[\w_][\w\d_]*/
"""


VAR_GRAMMAR_STRONG = r"""
start: (str | var)*
str: /([^\$]|(\$\W))+/
var: /\$[\w_][\w\d_]*/
"""


def magic(line: str, env: EnvironmentProcessor, grammar: str) -> str:

    # Парсим строку грамматикой
    lark = Lark(grammar)
    parsed = lark.parse(line)
    # заменяем переменные на значения и собираем строку обратно
    line = ''
    for token in parsed.children:
        token_value = str(token.children[0])
        line += env.get(token_value[1:]) if token.data == 'var' else token_value

    return line.rstrip()


def magic_light(line: str, env: EnvironmentProcessor) -> str:
    """
    Заменяет все переменные внутри строки на их значения, ЗА ИСКЛЮЧЕНИЕМ ТЕХ,ЧТО ОКРУЖЕНЫ КАВЫЧКАМИ
    :param line: строка
    :param env: процессор окружений
    :return: строка в которой все $VAL заменены на их значения или пустую строку.
    """
    return magic(line, env, VAR_GRAMMAR_LIGHT)


def magic_strong(line: str, env: EnvironmentProcessor) -> str:
    """
    Заменяет ВСЕ переменные внутри строки на их значения
    :param line: строка
    :param env: процессор окружений
    :return: строка в которой все $VAL заменены на их значения или пустую строку.
    """
    return magic(line, env, VAR_GRAMMAR_STRONG)

