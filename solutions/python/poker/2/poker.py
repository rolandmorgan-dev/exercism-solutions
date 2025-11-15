from collections import Counter

ORDER = {"2" : 2 ,"3": 3 ,"4": 4 ,"5": 5 ,"6": 6 ,"7": 7 ,"8": 8 ,"9": 9 ,"10": 10 ,"J": 11 ,"Q": 12 ,"K": 13 ,"A" : 14}
COMP_CARDS = "A,2,3,4,5,6,7,8,9,10,J,Q,K,A"

# return winners from straights
def winners_list(candidates, hands):
    counts_sum = []
    winners = []
    for candidate in candidates:
        hand_sum = sum((ORDER.get(value, 1) for value in candidate[0]))
        counts_sum.append((hand_sum, candidate[1]))
        
    max_sum = max(summ[0] for summ in counts_sum)
    for summ, index in counts_sum:
        if summ == max_sum:
            winners.append(hands[index])
    return winners

# return list of straights
def to_candidate(card_hand, i=None):
    iter_builder = []
    comp_hand = ",".join(card_hand)
    if comp_hand in COMP_CARDS:
        iter_builder.append((comp_hand.split(","), i))
    elif "A" in comp_hand and "A," + comp_hand[:-2] in COMP_CARDS:
        iter_builder.append((("1," + comp_hand[:-2]).split(","), i))
    return iter_builder

# return candidates, except for straights
def selector_loop(eval_no_A1, condition, func=lambda x: (x[1],x[0])):
    candidates = []
    for i, hand in enumerate(eval_no_A1):
        temp = Counter(hand)
        temp = sorted(temp.items(), key=func, reverse=True)
        if condition(temp):
            candidates.append((temp, i))
    return candidates

# return winners from non straights
def highest_wins(contesting_hands, hands, func=lambda x: (x[0],x[1])):
    scores_ordered = sorted(contesting_hands, key=func, reverse=True)
    highest = (scores_ordered[0])
    
    winners = []
    scores_ordered = sorted(scores_ordered, key= lambda x: x[1])
    for score in scores_ordered:
        if score[:-1] == highest[:-1]:
            winners.append(hands[score[-1]])
    return winners 


##########################
# choose best hand/hands #
##########################
def best_hands(hands):
    if len(hands) < 2: return hands
    
    cards = [[card[:-1] for card in chars.split()] for chars in hands]
    colors = [[color[-1] for color in chars.split()] for chars in hands]
    
    asc_cards = [sorted(i, key=lambda x: ORDER[x]) for i in cards]
    eval_no_A1 = [[ORDER.get(card, 0) for card in hand] for hand in asc_cards]
    
    # c_hands = contesting hands

    # check: straight flush
    if any(len(set(hand)) == 1 for hand in colors):
        c_hands = []
        for i, (card_hand, color_hand) in enumerate(zip(asc_cards, colors)):
            if len(set(color_hand)) == 1:
                if to_candidate(card_hand, i):
                    c_hands.append(*to_candidate(card_hand, i))
        if c_hands:
            return winners_list(c_hands, hands)
    
    # check: four of a kind
    if any(True for hand in asc_cards if len(set(hand[:-1])) == 1 or len(set(hand[1:])) == 1):
        condition = lambda temp: temp[0][1] == 4
        c_hands = (selector_loop(eval_no_A1, condition))
        return highest_wins(c_hands, hands)
    
    # check: full house
    if any(True for h in asc_cards if 3 in Counter(h).values() and 2 in Counter(h).values()):
        condition = lambda temp: temp[0][1] == 3 and temp[1][1] == 2
        c_hands = (selector_loop(eval_no_A1, condition))
        return highest_wins(c_hands, hands)
    
    # check: flush
    if any(len(set(hand)) == 1 for hand in colors):
        indexed_flush = [index for index, color in enumerate(colors) if len(set(color)) == 1]
        flush_hands = []
        for hand_num in range(len(hands)):
            if hand_num in indexed_flush:
                flush_hands.append(eval_no_A1[hand_num])
            else:
                flush_hands.append([])
        
        condition = lambda x: True 
        c_hands = (selector_loop(flush_hands, condition, func=lambda x: x[0]))
        return highest_wins(c_hands, hands)
    
    # check: straight
    if any(True for card in asc_cards if to_candidate(card)):
        c_hands = []
        for i, card in enumerate(asc_cards):
            if to_candidate(card, i):
                c_hands.append(*to_candidate(card, i))
        return winners_list(c_hands, hands)
    
    # check: three of a kind
    if any(True for hand in asc_cards if 3 in Counter(hand).values()):
        condition = lambda temp: temp[0][1] == 3
        c_hands = (selector_loop(eval_no_A1, condition))
        return highest_wins(c_hands, hands)
    
    # check: two pairs
    if any(True for hand in asc_cards if list(Counter(hand).values()).count(2) == 2):
        condition = lambda temp: temp[0][1] == 2 and temp[1][1] == 2
        c_hands = (selector_loop(eval_no_A1, condition))
        return highest_wins(c_hands, hands)
    
    # check: one pair
    if any(len(set(hand)) == 4 for hand in cards):
        condition = lambda temp: temp[0][1] == 2
        c_hands = (selector_loop(eval_no_A1, condition))
        return highest_wins(c_hands, hands)
    
    # high card
    c_hands = (selector_loop(eval_no_A1, lambda x: True, lambda x: x[0]))
    return highest_wins(c_hands, hands)
