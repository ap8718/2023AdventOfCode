INPUT_FILENAME = "day9_input.txt"

def is_list_zero(num_list):
    return all([n == 0 for n in num_list])
    

def get_differences_and_return_sum_of_last_digits(num_list):
    diff_list = []
    for i in range(len(num_list)-1):
        diff_list.append(num_list[i+1] - num_list[i])

    if is_list_zero(diff_list):
        return num_list[-1]
    
    return get_differences_and_return_sum_of_last_digits(diff_list) + num_list[-1]
    

def fill_out_inverse_pyramid(line):
    num_list = [int(n) for n in line.split(' ')]
    return get_differences_and_return_sum_of_last_digits(num_list)


if __name__ == "__main__":
    input_file = open(INPUT_FILENAME, 'r')
    Lines = input_file.readlines()

    sum_of_values = 0

    for line in Lines:
        sum_of_values += fill_out_inverse_pyramid(line)

    print(sum_of_values)
