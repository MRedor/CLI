import unittest
import os

from commands.comands import get_command_by_name

from io import BytesIO
from environment_processor import EnvironmentProcessor
from typing import Callable, BinaryIO, List

Command = Callable[[BinaryIO, BinaryIO, EnvironmentProcessor, List[str]], None]

def run_and_get_result(cmd: Command, stdin_bytes: bytes, argv: List[str]) -> bytes:
    """
    Run cmd(BytesIO(stdin_str), stdout, env, argv) and return stdout.getvalue()
    :param cmd: command to run
    :param stdin_bytes: data to stdin stream
    :param argv: command run arguments
    :return: data from output stream
    """
    env = EnvironmentProcessor()
    stdout = BytesIO()

    stdin = BytesIO(stdin_bytes)
    cmd(stdin, stdout, env, argv)
    return stdout.getvalue()

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

class CatCommandTests(unittest.TestCase):

    def test_empty_file(self):
        cat = get_command_by_name('cat')
        path = os.path.join(THIS_DIR, 'test_data', 'empty.txt')
        self.assertEqual(run_and_get_result(cat, b'', ['cat', path]), b'')

    def test_file(self):
        cat = get_command_by_name('cat')
        path = os.path.join(THIS_DIR, 'test_data', 'unittest_doc.txt')
        with open(path, 'rb') as file:
            out_expected = file.read()
        out = run_and_get_result(cat, b'', ['cat', path])
        self.assertEqual(out, out_expected)

    def test_empty_stdin(self):
        cat = get_command_by_name('cat')
        self.assertEqual(run_and_get_result(cat, b'', ['cat']), b'')

    def test_stdin(self):
        cat = get_command_by_name('cat')
        self.assertEqual(run_and_get_result(cat, b'some\ndata\n\n', ['cat']), b'some\ndata\n\n')

class WcCommandTests(unittest.TestCase):
    # тут в не пустых тестах ответ посчитан просто линуксовым вызовом wc
    def test_empty_file(self):
        wc = get_command_by_name('wc')
        path = os.path.join(THIS_DIR, 'test_data', 'empty.txt')
        self.assertEqual(run_and_get_result(wc, b'', ['wc', path]), b'    0    0    0\n')

    def test_file(self):
        wc = get_command_by_name('wc')
        path = os.path.join(THIS_DIR, 'test_data', 'unittest_doc.txt')
        self.assertEqual(run_and_get_result(wc, b'', ['wc', path]), b'    1822    11107    82950\n')

    def test_empty_stdin(self):
        wc = get_command_by_name('wc')
        self.assertEqual(run_and_get_result(wc, b'', ['wc']), b'    0    0    0\n')

    def test_stdin(self):
        wc = get_command_by_name('wc')

        path = os.path.join(THIS_DIR, 'test_data', 'unittest_doc.txt')
        with open(path, 'rb') as file:
            self.assertEqual(run_and_get_result(wc, file.read(), ['wc']), b'    1822    11107    82950\n')

class ExitTests(unittest.TestCase):
    # Проверяем что exit не убивает ничего и просто меняет env.exit
    def test_exit(self):
        cmd = get_command_by_name('exit')
        env = EnvironmentProcessor()
        self.assertFalse(env.exit)
        cmd(BytesIO(), BytesIO(), env, ['exit'])
        self.assertTrue(env.exit)

class EchoTests(unittest.TestCase):

    def test_empty(self):
        echo = get_command_by_name('echo')
        self.assertEqual(run_and_get_result(echo, b'', ['echo']), b'')

    def test_one(self):
        echo = get_command_by_name('echo')
        self.assertEqual(run_and_get_result(echo, b'', ['echo', 'wc']), b'wc')

    def test_many(self):
        echo = get_command_by_name('echo')
        self.assertEqual(run_and_get_result(echo, b'', ['echo', 'one  two', "three  four", '  five']), b'one  two three  four   five')

class PwdTests(unittest.TestCase):
    # тут как то тупо тестить. позову pwd и сравню с тем что питон говорит. но внутри pwd этоработает ровно так же
    def test_strange(self):
        pwd = get_command_by_name('pwd')
        real_path = os.getcwd()
        self.assertEqual(run_and_get_result(pwd, b'', ['pwd']), real_path.encode() + b'\n')

if __name__ == '__main__':
    unittest.main()
