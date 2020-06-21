from shell.shell import Shell

import sys


def main():
    shell = Shell(sys.stdin, sys.stdout)
    shell.start()


if __name__ == "__main__":
    main()
