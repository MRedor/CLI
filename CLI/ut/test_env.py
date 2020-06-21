import random
import string
import unittest

from environment_processor import EnvironmentProcessor


class MyTestCase(unittest.TestCase):
    def test_env(self):
        env =  EnvironmentProcessor()
        var_name = ''.join(random.choices(string.ascii_lowercase, k=100))
        self.assertEqual('', env.get(var_name))
        for _ in range(10):
            value = ''.join(random.choices(string.ascii_uppercase + ' ', k=100))
            env.set(var_name, value)
            self.assertEqual(value, env.get(var_name))


if __name__ == '__main__':
    unittest.main()
