from scripts.game import *


def test_get_rounds_27():
    assert get_rounds(27) == [27, 28, 29]


def test_concatenate_rounds_1():
    assert concatenate_rounds([27, 28, 29], [35, 36]) == [27, 28, 29, 35, 36]


def test_list_contains_round_29_True():
    assert list_contains_round([27, 28, 29, 35, 36], 29) == True


def test_list_contains_round_30_False():
    assert list_contains_round([27, 28, 29, 35, 36], 30) == False


def test_card_average_6():
    assert card_average([5, 6, 7]) == 6.0


def test_approx_average_is_average_1_True():
    assert approx_average_is_average([1, 2, 3]) == True


def test_approx_average_is_average_2_True():
    assert approx_average_is_average([2, 3, 4, 8, 8]) == True
