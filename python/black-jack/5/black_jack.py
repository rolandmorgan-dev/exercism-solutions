"""Functions to help play and score a game of blackjack."""

def value_of_card(card):
    # Determine the scoring value of a card.
    if card in "JQK":
        return 10
    if card == "A":
        return 1
    if card.isdigit() and 1 < int(card) < 11:
        return int(card)
    raise ValueError("Wrong Input")

def higher_card(card_one, card_two):
    # Which card is higher
    first, second = value_of_card(card_one), value_of_card(card_two)
    if first == second:
        return (card_one, card_two)
    if first > second:
        return card_one
    return card_two

def value_of_ace(card_one, card_two):
    # Ace value
    score_needed = 21 - (value_of_card(card_one) + value_of_card(card_two))
    if card_one == "A" or card_two == "A":
        return 1
    if score_needed > 10:
        return 11
    return 1

def is_blackjack(card_one, card_two):
    # Natural or Blackjack
    if value_of_card(card_one) == 1 and value_of_card(card_two) == 10:
        return True
    if value_of_card(card_one) == 10 and value_of_card(card_two) == 1:
        return True
    return False

def can_split_pairs(card_one, card_two):
    # Splitting pairs
    if value_of_card(card_one) == value_of_card(card_two):
        return True
    return False

def can_double_down(card_one, card_two):
    # Can double down the bet or not, check.
    if 8 < (value_of_card(card_one) + value_of_card(card_two)) < 12 :
        return True
    return False