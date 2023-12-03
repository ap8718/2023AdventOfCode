import re

MAX_RED_COUNT = 12
MAX_GREEN_COUNT = 13
MAX_BLUE_COUNT = 14

ID_MATCH_PATTERN = "Game (.*)"

RED_MATCH_PATTERN = "(.*) red"
GREEN_MATCH_PATTERN = "(.*) green"
BLUE_MATCH_PATTERN = "(.*) blue"

FILENAME = 'day2_input.txt'


def extract_id_games_from_line(line):
    id_game = line.split(':')

    match = re.match(ID_MATCH_PATTERN, id_game[0])
    id = int(match.group(1))

    game = id_game[1].split(';')

    return id, game


def get_rgb_count_from_subgame(subgame):
    turns = subgame.split(',')

    red_count = 0
    green_count = 0
    blue_count = 0

    for turn in turns:

        red_match = re.match(RED_MATCH_PATTERN, turn)
        if red_match:
            red_count = int(red_match.group(1))
            continue

        green_match = re.match(GREEN_MATCH_PATTERN, turn)
        if green_match:
            green_count = int(green_match.group(1))
            continue

        blue_match = re.match(BLUE_MATCH_PATTERN, turn)
        if blue_match:
            blue_count = int(blue_match.group(1))
            continue

    return red_count, green_count, blue_count


def main(input_filename):
    input_file = open(input_filename, 'r')
    Lines = input_file.readlines()

    sum_of_ids = 0

    for line in Lines:

        game_possible = True

        line = line[:-1]    # Get rid of \n

        id, game = extract_id_games_from_line(line)

        for subgame in game:
            red_count, green_count, blue_count = get_rgb_count_from_subgame(subgame)

            game_possible = red_count <= MAX_RED_COUNT and green_count <= MAX_GREEN_COUNT and blue_count <= MAX_BLUE_COUNT
            if not game_possible:
                break

        if game_possible:
            sum_of_ids += id

    print(sum_of_ids)


if __name__ == "__main__":
    main(FILENAME)
