import os
import sys
from contextlib import contextmanager
from io import StringIO

from matriz import main


@contextmanager
def replace_stdin(target):
    orig = sys.stdin
    sys.stdin = target
    yield
    sys.stdin = orig


def run(capsys, commands, monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['matriz.py'])
    with replace_stdin(commands):
        main()
    out, _ = capsys.readouterr()
    return out


def test_matriz(capsys, monkeypatch):
    with open('input.txt') as file:
        commands = StringIO(file.read())
    run(capsys, commands, monkeypatch)

    with open('test_1.txt') as test_1:
        assert test_1.read() == 'OOOOO\nOOOOO\nOAOOO\nOOOOO\nOOOOO\nOOOOO\n'

    with open('test_2.txt') as test_2:
        assert test_2.read() == 'JJJJJ\nJJZZJ\nJWJJJ\nJWJJJ\nJJJJJ\nJJJJJ\n'

    with open('test_3.txt') as test_3:
        assert test_3.read() == 'JJJJJJJJJJ\nJJJJJJJJJJ\nJWJJAJJJJJ\nJWJJJJJJJJ\nZZZZZZZZZZ\n' \
                                'RRRRRRRRRR\nREEEEEEERR\nREEEEEEERR\nRRRRRRRRRR\n'

    os.remove('test_1.txt')
    os.remove('test_2.txt')
    os.remove('test_3.txt')
