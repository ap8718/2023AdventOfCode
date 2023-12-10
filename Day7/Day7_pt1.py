INPUT_FILENAME = "day7_input.txt"
CARDS = [
    'A',
    'K',
    'Q',
    'J',
    'T',
    '9',
    '8',
    '7',
    '6',
    '5',
    '4',
    '3',
    '2'
]

FIVE_OF_A_KIND = []
FOUR_OF_A_KIND = []
FULL_HOUSE = []
THREE_OF_A_KIND = []
TWO_PAIR = []
ONE_PAIR = []
HIGH_CARD = []


def find_where(elem, List):
    return [i for i in range(len(List)) if elem == List[i]][0]

def stronger_card(cardA, cardB):
    idxA = find_where(cardA, CARDS) 
    idxB = find_where(cardB, CARDS)
    if idxA < idxB:
        return cardA
    elif idxA > idxB:
        return cardB
    return 'EQUAL'

def get_hand(cards_str):
    hand = dict({})
    for c in cards_str:
        if c not in hand:
            hand[c] = 0
        hand[c] += 1

    return hand

def append_hand_to_category(cards_str):

    hand = get_hand(cards_str)

    if 5 in hand.values():
        FIVE_OF_A_KIND.append(cards_str)
    elif 4 in hand.values():
        FOUR_OF_A_KIND.append(cards_str)
    elif 3 in hand.values() and 2 in hand.values():
        FULL_HOUSE.append(cards_str)
    elif 3 in hand.values() and 1 in hand.values():
        THREE_OF_A_KIND.append(cards_str)
    elif 2 in hand.values() and len(hand) == 3:
        TWO_PAIR.append(cards_str)
    elif 2 in hand.values() and len(hand) == 4:
        ONE_PAIR.append(cards_str)
    else:
        HIGH_CARD.append(cards_str)
    
    return

def get_cards_and_bid_from_line(line):
    split_line = line.split(' ')
    return split_line[0], split_line[1]

input_file = open(INPUT_FILENAME, 'r')
Lines = input_file.readlines()

for line in Lines:
    cards, bid = get_cards_and_bid_from_line(line)
    append_hand_to_category(cards)

print("FIVE_OF_A_KIND: ", FIVE_OF_A_KIND)
print("FOUR_OF_A_KIND: ", FOUR_OF_A_KIND)
print("FULL_HOUSE: ", FULL_HOUSE)
print("THREE_OF_A_KIND: ", THREE_OF_A_KIND)
print("TWO_PAIR: ", TWO_PAIR)
print("ONE_PAIR: ", ONE_PAIR)
print("HIGH_CARD: ", HIGH_CARD)
