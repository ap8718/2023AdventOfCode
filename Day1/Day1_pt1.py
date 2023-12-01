FILENAME = 'day1_input.txt'

input_file = open(FILENAME, 'r')
Lines = input_file.readlines()

sum_of_calib_values = 0

for line in Lines:
    list_of_digits = [c for c in line if c.isdigit()]
    calib_value = int(list_of_digits[0] + list_of_digits[-1])
    sum_of_calib_values += calib_value

print(sum_of_calib_values)
