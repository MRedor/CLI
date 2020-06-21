from .cat import cat
from .echo import echo
from .exit import exit_command
from .pwd import pwd
from .unknown import unknown
from .wc import wc

from environment_processor import EnvironmentProcessor

from typing import BinaryIO
from typing import Callable
from typing import List

def get_command_by_name(name: str) -> Callable[[BinaryIO, BinaryIO, EnvironmentProcessor, List[str]], None]:
    commands = {
        'cat': cat,
        'echo': echo,
        'exit': exit_command,
        'pwd': pwd,
        'wc': wc
    }
    return commands.get(name, unknown)
