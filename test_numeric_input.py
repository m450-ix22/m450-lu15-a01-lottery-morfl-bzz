import pytest
from numeric_input import read_int, read_float


def test_read_int_valid_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '5')
    assert read_int("Enter a number", 1, 10) == 5
