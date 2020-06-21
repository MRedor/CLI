from lark.tree import Tree
from typing import Union
from typing import BinaryIO
from io import BytesIO
from environment_processor import EnvironmentProcessor

from commands.comands import get_command_by_name
from shell.magic import magic


def line(expr: Union[Tree, Tree], stdin: BinaryIO, stdout: BinaryIO, env: EnvironmentProcessor) -> None:
    if expr.data != 'line':
        raise Exception('not pipe expression')
    if expr.children[0].data == 'pipe':
        pipe(expr.children[0], stdin, stdout, env)
    elif expr.children[0].data == 'simple':
        simple(expr.children[0], stdin, stdout, env)
    else:
        raise Exception('trash line syntax')


def pipe(expr: Union[Tree, Tree], stdin: BinaryIO, stdout: BinaryIO, env: EnvironmentProcessor) -> None:
    if expr.data != 'pipe':
        raise Exception('not pipe expression')

    # левая часть всегда simple
    left = expr.children[0]
    left_out = BytesIO()
    simple(left, stdin, left_out, env)

    # правая часть всегда line
    right_in = BytesIO(left_out.getvalue())
    right = expr.children[1]
    line(right, right_in, stdout, env)


def simple(expr: Union[Tree, Tree], stdin: BinaryIO, stdout: BinaryIO, env: EnvironmentProcessor) -> None:
    if expr.data != 'simple':
        raise Exception('not simple expression')

    simple_child = expr.children[0]
    if simple_child.data == 'declaration':
        declaration(simple_child, env)
    elif simple_child.data == 'command':
        command(simple_child, stdin, stdout, env)
    else:
        raise Exception('trash token')


def command(expr: Union[Tree, Tree], stdin: BinaryIO, stdout: BinaryIO, env: EnvironmentProcessor) -> None:
    if expr.data != 'command':
        raise Exception('not command token')

    argv = []
    for str_tree in expr.children:
        argv.append(str_tree_to_str(str_tree, env))

    # print(argv)
    command_func = get_command_by_name(argv[0])
    command_func(stdin, stdout, env, argv)


def declaration(expr: Union[Tree, Tree], env: EnvironmentProcessor) -> None:
    if expr.data != 'declaration':
        raise Exception('not declaration token')

    name = str_tree_to_str(expr.children[0], env)
    val = str_tree_to_str(expr.children[1], env)
    env.set(name, val)


def str_tree_to_str(str_tree: Tree, env: EnvironmentProcessor) -> str:
    result_str = ''
    for child in str_tree.children:
        if child.data == 'lq':
            result_str += magic(str(child.children[0])[1:-1], env)
        elif child.data == 'sq':
            result_str += str(child.children[0])[1:-1]
        elif child.data == 'word':
            result_str += str(child.children[0])
        else:
            raise Exception('wrong str token')
    return result_str


def run(expr: Union[Tree, Tree], stdin: BinaryIO, stdout: BinaryIO, env: EnvironmentProcessor) -> None:
    if expr.children[0].data == 'empty':
        return
    elif expr.children[0].data == 'line':
        line(expr.children[0], stdin, stdout, env)
    else:
        raise Exception('wrong start token')
