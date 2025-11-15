from collections import Counter

ORDER = {"2" : 2 ,"3": 3 ,"4": 4 ,"5": 5 ,"6": 6 ,"7": 7 ,"8": 8 ,"9": 9 ,"10": 10 ,"J": 11 ,"Q": 12 ,"K": 13 ,"A" : 14}
COMP_CARDS = "A,2,3,4,5,6,7,8,9,10,J,Q,K,A"


# return winners from straight counts
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


# return list of straight counts
def to_candidate(card_hand, i=None):
    iter_builder = []
    comp_hand = ",".join(card_hand)
    if comp_hand in COMP_CARDS:
        iter_builder.append((comp_hand.split(","), i))
    elif "A" in comp_hand and "A," + comp_hand[:-2] in COMP_CARDS:
        iter_builder.append((("1," + comp_hand[:-2]).split(","), i))
    return iter_builder


# return winners from: full house,(pairs:four,three,two,one),high card
def highest_wins(counts, hands):
    scores_ordered = sorted(counts, key= lambda x: (x[0],x[1]), reverse=True)
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
    evaluated = [[ORDER.get(card, 0) for card in hand] for hand in asc_cards]
    counts = []
    
    # check: straight flush
    if any(len(set(hand)) == 1 for hand in colors):
        print("straight flush")
        for i, (card_hand, color_hand) in enumerate(zip(asc_cards, colors)):
            if len(set(color_hand)) == 1:
                if to_candidate(card_hand, i):
                    counts.append(*to_candidate(card_hand, i))
        if counts:
            return winners_list(counts, hands)
    
    # check: four of a kind
    if any(True for hand in asc_cards if len(set(hand[:-1])) == 1 or len(set(hand[1:])) == 1):
        print("four of a kind")
        for i, hand in enumerate(evaluated):
            temp = Counter(hand)
            temp = sorted(temp.items(), key= lambda x: (x[1],x[0]), reverse=True)
            if temp[0][1] == 4:
                counts.append((temp[0][0],temp[1][0], i))
        
        if counts:
            return highest_wins(counts, hands)
    
    # check: full house
    if any(True for h in asc_cards if 3 in Counter(h).values() and 2 in Counter(h).values()):
        print("full house")
        for i, hand in enumerate(evaluated):
            temp = Counter(hand)
            temp = sorted(temp.items(), key= lambda x: (x[1],x[0]), reverse=True)
            if temp[0][1] == 3:
                counts.append((temp[0][0],temp[1][0], i))
        
        if counts:
            return highest_wins(counts, hands)
    
    # check: flush
    if any(len(set(hand)) == 1 for hand in colors):
        print("flush")
        for i, (card_hand, color_hand) in enumerate(zip(evaluated, colors)):
            if len(set(color_hand)) == 1:
                counts.append((card_hand, i))
                
        highest = counts[0][0]
        winners = []
        for score in counts:
            if score[0] == highest:
                winners.append(hands[score[1]])
        return winners
    
    # check: straight
    if any(True for card in asc_cards if to_candidate(card)):
        print("straight")
        for i, card in enumerate(asc_cards):
            if to_candidate(card, i):
                counts.append(*to_candidate(card, i))
        if counts:
            return winners_list(counts, hands)
    
    # check: three of a kind
    if any(True for hand in asc_cards if 3 in Counter(hand).values()):
        print("three of a kind")
        for i, hand in enumerate(evaluated):
            temp = Counter(hand)
            temp = sorted(temp.items(), key= lambda x: (x[1],x[0]), reverse=True)
            if temp[0][1] == 3:
                counts.append((temp, i))
        if counts:
            return highest_wins(counts, hands)
    
    # check: two pairs
    if any(True for hand in asc_cards if list(Counter(hand).values()).count(2) == 2):
        print("two pairs")
        for i, hand in enumerate(evaluated):
            temp = Counter(hand)
            temp = sorted(temp.items(), key= lambda x: (x[1],x[0]), reverse=True)
            print(temp)
            if temp[0][1] == 2 and temp[1][1] == 2:
                counts.append((temp, i))
        if counts:
            return highest_wins(counts, hands)
    
    # check: one pair
    if any(len(set(hand)) == 4 for hand in cards):
        print("one pair")
        for i, hand in enumerate(evaluated):
            temp = Counter(hand)
            temp = sorted(temp.items(), key= lambda x: (x[1],x[0]), reverse=True)
            if temp[0][1] == 2:
                counts.append((temp, i))
                
        if counts:
            return highest_wins(counts, hands)
    
    # high card
    for i, hand in enumerate(evaluated):
        print("high card")
        temp = Counter(hand)
        temp = sorted(temp.items(), key= lambda x: x[0], reverse=True)
        counts.append((temp, i))
    return highest_wins(counts, hands)