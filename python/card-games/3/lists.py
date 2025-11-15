"""Functions for tracking poker hands and assorted card tasks."""


def get_rounds(number) -> int:
    # Returning a three element list, first: number, second: number+1, third: number+2
    return [number, number+1, number+2]

def concatenate_rounds(rounds_1, rounds_2):
    # Two list merged into a single list
    return rounds_1 + rounds_2

def list_contains_round(rounds, number):
    # Check if the round has been already played
    return number in rounds

def card_average(hand):
    # Average of the card values
    return sum(hand) / len(hand)

def approx_average_is_average(hand):
    # Checking if the average of first & last number equal with the whole average
    # or median (middle card) value equal with the whole average
    return (hand[0]+hand[-1])/2 == card_average(hand) or \
    hand[int(len(hand)/2 -0.5)] == card_average(hand)

def average_even_is_average_odd(hand):
    # Returning True if even & odd numbers average is equal, False otherwise
    return sum(hand[::2])/len(hand[::2]) == sum(hand[1::2])/len(hand[1::2])

def maybe_double_last(hand):
    # If last card value 11, double it, return list with doubled last value
    # else return the original list
    if hand[-1] == 11: hand[-1] *= 2
    return hand