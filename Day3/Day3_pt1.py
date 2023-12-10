INPUT_FILE = "day3_input.txt"

input_file = open(INPUT_FILE, 'r')
Lines = input_file.readlines()

print([c for c in Lines[0]])
