INPUT_FILENAME = "day4_input.txt"

def get_score_from_matches(matches):
    if matches == 0:
        return 0
    return 2**(matches-1)


def get_winning_cards_and_hand_from_line(line):
    line = line[:-1]
    id_and_cards = line.split(':')
    cards = id_and_cards[1]
    winning_and_hand = cards.split('|')
    winning_cards = winning_and_hand[0]
    cards_in_hand = winning_and_hand[1]
    winning_cards = winning_cards.split(' ')
    cards_in_hand = cards_in_hand.split(' ')
    winning_cards = {c for c in winning_cards if c != ''}
    cards_in_hand = {c for c in cards_in_hand if c != ''}
    return winning_cards, cards_in_hand


def main():
    input_file = open(INPUT_FILENAME, 'r')
    Lines = input_file.readlines()
    total_points = 0

    for line in Lines:
        winning_cards, hand = get_winning_cards_and_hand_from_line(line)
        set_of_matches = winning_cards.intersection(hand)
        matches = len(set_of_matches)

        score = get_score_from_matches(matches)
        total_points += score

    print(total_points)

if __name__ == "__main__":
    main()
