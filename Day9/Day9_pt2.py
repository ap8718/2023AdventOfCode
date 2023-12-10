from Day9_pt1 import (
    INPUT_FILENAME,
    is_list_zero,
)

def get_differences_and_return_diff_of_first_digits(num_list):
    diff_list = []
    for i in range(len(num_list)-1):
        diff_list.append(num_list[i+1] - num_list[i])

    if is_list_zero(diff_list):
        return num_list[0]
    
    return num_list[0] - get_differences_and_return_diff_of_first_digits(diff_list)
    

def fill_out_inverse_pyramid(line):
    num_list = [int(n) for n in line.split(' ')]
    return get_differences_and_return_diff_of_first_digits(num_list)

if __name__ == "__main__":
    input_file = open(INPUT_FILENAME, 'r')
    Lines = input_file.readlines()

    sum_of_values = 0

    for line in Lines:
        sum_of_values += fill_out_inverse_pyramid(line)

    print(sum_of_values)