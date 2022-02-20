import math


def get_rounds(round_number: int) -> list:
    return [round_number, round_number+1, round_number+2]


def concatenate_rounds(rounds_1: list, rounds_2: list) -> list:
    return rounds_1 + rounds_2


def list_contains_round(rounds: list, round_number: int) -> bool:
    return round_number in rounds


def card_average(hand: list) -> float:
    return sum(hand)/len(hand)


def approx_average_is_average(hand: list) -> bool:
    """
    Returns True if either:
    - the average of the first and last number in the had equals the real average
    - the middle card equals the real average
    """
    if card_average(hand) == (hand[0] + hand[-1])/2:
        return True
    return len(hand) % 2 != 0 and hand[math.ceil(len(hand) // 2)] == card_average(hand)


def average_even_is_average_odd(hand: list) -> bool:
    """
    Returns True if the average of the even positions equals the average of the odd
    positions
    """
    return card_average(hand[::2]) == card_average(hand[1::2])


def maybe_double_last(hand: list) -> list:
    if hand[-1] == 11:
        hand[-1] = 22
    return hand
