import unittest

from shell.shell import Shell
from io import StringIO


def run_and_get_result(stdin_str):
    stdin = StringIO(stdin_str)
    stdout = StringIO()
    Shell(stdin, stdout).start()
    return stdout.getvalue()


class MyTestCase(unittest.TestCase):
    def test_var(self):
        self.assertEqual(run_and_get_result('a=10\necho $a\nexit\n'), '10')
        self.assertEqual(run_and_get_result('a=\'$a\'\necho $a"$a"\'$a\'\nexit\n'), '$a$a$a')  # ahah!
        self.assertEqual(run_and_get_result('a=\'a\'\necho $a"$a"\'$a\'\nexit\n'), 'aa$a')
        self.assertEqual(run_and_get_result('a=echo\n$a "$a"\nexit\n'), 'echo')
        self.assertEqual(run_and_get_result('a=a\nb=b\nb=$a$b\necho $b\nexit\n'), 'ab')
        self.assertEqual(run_and_get_result('ho=ho\nec$ho success\nexit\n'), 'success')

    def test_quotes(self):
        self.assertEqual(run_and_get_result('"echo" success\nexit'), 'success')
        self.assertEqual(run_and_get_result('\'echo\' success\nexit'), 'success')
        self.assertNotEqual(run_and_get_result('\'echo \'success\nexit'), 'success')

        self.assertEqual(run_and_get_result('echo s"u"c\'c\'e"ss"\nexit'), 'success')

        self.assertEqual(run_and_get_result('a="success"\necho $a\nexit'), 'success')
        self.assertEqual(run_and_get_result('a="success"\necho "$a"\nexit'), 'success')
        self.assertNotEqual(run_and_get_result('a="success"\necho \'$a\'\nexit'), 'success')

    def test_pipe(self):
        self.assertEqual(run_and_get_result('echo success | cat\nexit'), 'success')
        self.assertEqual(run_and_get_result('echo success | cat | cat\nexit'), 'success')
        self.assertEqual(run_and_get_result('echo success|cat\nexit'), 'success')
        self.assertEqual(run_and_get_result('echo success|cat|cat\nexit'), 'success')

        self.assertEqual(run_and_get_result('echo success | wc | cat\nexit'), '    0    1    7\n')
        self.assertEqual(run_and_get_result('echo success | wc | wc | cat\nexit'), '    1    3    16\n')


if __name__ == '__main__':
    unittest.main()
