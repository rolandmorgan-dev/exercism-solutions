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
    # 1.Sorting the given list
    # 2.Checking if the average of first & last number equal with the whole average
    # or median (middle card) value equal with the whole average
    hand.sort()
    return (hand[0]+hand[-1])/2 == card_average(hand) or \
    hand[int(len(hand)/2 -0.5)] == card_average(hand)

def average_even_is_average_odd(hand):
    # Creating list objects, then iterating over the even & odd numbers, seperatedly
    # returning True if even & odd numbers average is equal
    evens=[]
    odds=[]
    for even in hand[0::2]:
        evens.append(even)
    for odd in hand[1::2]:
        odds.append(odd)
    return sum(evens)/len(evens) == sum(odds)/len(odds)

def maybe_double_last(hand):
    # If last card value 11, double it, return list with doubled last value
    if hand[len(hand)-1] == 11:
        hand[len(hand)-1] *= 2
    return hand