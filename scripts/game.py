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
    average = sum(hand)/len(hand)
    if average == (hand[0] + hand[-1])/2:
        return True
    return len(hand) % 2 != 0 and math.ceil(len(hand)) == average
