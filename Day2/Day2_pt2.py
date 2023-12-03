from Day2_pt1 import (
    extract_id_games_from_line,
    get_rgb_count_from_subgame
)

FILENAME = 'day2_input.txt'

def main(input_filename):
    input_file = open(input_filename, 'r')
    Lines = input_file.readlines()

    sum_of_powers = 0

    for line in Lines:

        max_red_count = 0
        max_green_count = 0
        max_blue_count = 0

        line = line[:-1]    # Get rid of \n

        _, game = extract_id_games_from_line(line)

        for subgame in game:
            red_count, green_count, blue_count = get_rgb_count_from_subgame(subgame)
            max_red_count = max(max_red_count, red_count)
            max_green_count = max(max_green_count, green_count)
            max_blue_count = max(max_blue_count, blue_count)

        power_of_set = max_red_count*max_blue_count*max_green_count
        sum_of_powers += power_of_set

    print(sum_of_powers)

if __name__ == "__main__":
    main(FILENAME)
