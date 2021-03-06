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


def test_approx_average_is_average_3_False():
    assert approx_average_is_average([1, 2, 3, 5, 9]) == False


def test_approx_average_is_average_4_True():
    assert approx_average_is_average([9, 2, 5, 1, 8]) == True


def test_approx_average_is_aerage_5_True():
    assert approx_average_is_average([1, 2, 4, 5, 8]) == True


def test_approx_average_is_average_even_list_True():
    assert approx_average_is_average([1, 3, 3, 3]) == False


def test_average_even_is_average_odd():
    assert average_even_is_average_odd([1, 2, 3]) == True


def test_average_even_is_average_odd_2():
    assert average_even_is_average_odd([1, 2, 3, 4]) == False


def test_maybe_double_last_double():
    assert maybe_double_last([5, 9, 11]) == [5, 9, 22]


def test_maybe_double_last_no_double():
    assert maybe_double_last([5, 9, 10]) == [5, 9, 10]
