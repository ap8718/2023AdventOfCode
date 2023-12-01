DIGITS_AND_WORDS = {
    '0': '0',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

FILENAME = 'day1_input.txt'
BUFFER_LENGTH = 5

def extract_num_in_word(num_in_word):
    for i in range(len(num_in_word)):
        if num_in_word[i]:
            return list(DIGITS_AND_WORDS.values())[i]
        

input_file = open(FILENAME, 'r')
Lines = input_file.readlines()
sum_of_calib_values = 0

for line in Lines:
    calib_value = ''
    line_len = len(line)
    buffer_length = min(BUFFER_LENGTH, line_len)

    # Slide buffer to the left until we find number
    for i in range(-buffer_length+1, line_len):
        # Start with buffer size 1, then 2, ..., until buffer_length, then constant buffer size
        buffer = line[max(0, i):i+buffer_length]
        num_in_word = [num in buffer for num in DIGITS_AND_WORDS]
        if True in num_in_word:
            digit = extract_num_in_word(num_in_word)
            calib_value += digit
            break

    # Slide buffer to the right until we find number
    for i in range(-buffer_length+1, line_len):
        # Start with buffer size 1, then 2, ..., until buffer_length, then constant buffer size
        buffer = line[line_len-1-i:min(line_len+buffer_length-1-i, line_len)]
        num_in_word = [num in buffer for num in DIGITS_AND_WORDS]
        if True in num_in_word:
            digit = extract_num_in_word(num_in_word)
            calib_value += digit
            break

    sum_of_calib_values += int(calib_value)

print(sum_of_calib_values)
