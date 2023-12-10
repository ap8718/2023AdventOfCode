import re
INPUT_FILENAME = "day8_input.txt"

input_file = open(INPUT_FILENAME, 'r')
Lines = input_file.readlines()

INSTRUCTIONS = Lines[0][:-1]    # First line is instructions, and get rid of \n

Lines = Lines[2:]

def split_line_into_node_branches(line):
    pattern = "(\w+) = (.*)"
    match = re.match(pattern, line)
    if not match:
        return "", ("", "")
    node = match.group(1)
    branches = match.group(2)
    branches = branches[1:-1].split(", ")

    return node, (branches[0], branches[1])

def create_node_mapping_dict(Lines):
    mapping_dict = dict({})
    for line in Lines:
        node, branches = split_line_into_node_branches(line)
        mapping_dict[node] = branches

    return mapping_dict

def find_num_steps_to_goal_node(start_node, goal_node):
    node = start_node
    num_steps = 0
    len_instructions = len(INSTRUCTIONS)

    while True:
        instr = INSTRUCTIONS[num_steps % len_instructions]
        branches = MAPPING_DICT[node]
        
        if instr == 'L':
            node = branches[0]
        elif instr == 'R':
            node = branches[1]

        num_steps += 1
        if node == goal_node:
            return num_steps

MAPPING_DICT = create_node_mapping_dict(Lines)

if __name__ == "__main__":
    start_node = 'AAA'
    goal_node = 'ZZZ'

    num_steps = find_num_steps_to_goal_node(start_node, goal_node)

    print("pt 1: ", num_steps)
