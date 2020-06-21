import os

class EnvironmentProcessor:
    def __init__(self):
        self.exit = False

    def get(self, key: str) -> str:
        """
        Достает из environ значение переменной. Если такой переменной нет возвращает пустую строку.
        :param key: имя переменной
        :return: значение
        """
        return os.environ.get(key, '')

    def set(self, key: str, value: str) -> None:
        """
        Устанавливает значение переменной в environ
        :param key: имя
        :param value: значение
        """
        os.environ[key] = value
