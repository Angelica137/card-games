from scripts.game import *


def test_get_rounds_27():
    assert get_rounds(27) == [27, 28, 29]


def test_concatenate_rounds_1():
    assert concatenate_rounds([[27, 28, 29], [35, 36]]) == [27, 28, 29, 35, 36]
