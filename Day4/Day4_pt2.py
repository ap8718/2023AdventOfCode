from Day4_pt1 import (
    INPUT_FILENAME,
    get_winning_cards_and_hand_from_line
)


def get_num_matches(Lines, i):

    winning_cards, hand = get_winning_cards_and_hand_from_line(Lines[i])
    set_of_matches = winning_cards.intersection(hand)
    num_matches = len(set_of_matches)
    # print(i, num_matches)
    num_copies = 0

    for j in range(num_matches):
        num_copies += get_num_matches(Lines, i+j+1)

    return num_copies + 1


def main():
    input_file = open(INPUT_FILENAME, 'r')
    Lines = input_file.readlines()
    total_cards = 0
    # print(Lines)
    for i in range(len(Lines)):
        total_cards += get_num_matches(Lines, i)
    print(total_cards)

if __name__ == "__main__":
    main()

