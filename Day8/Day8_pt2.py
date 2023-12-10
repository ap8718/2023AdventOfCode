from Day8_pt1 import (
    create_node_mapping_dict,

    INPUT_FILENAME
)

def get_list_of_starting_nodes(mapping_dict):
    return [node for node in mapping_dict if node[-1] == 'A']

def goal_reached(nodes):

    len_nodes = len(nodes)
    z_nodes = [node for node in nodes if node[-1] == 'Z']
    print(z_nodes)
    return len(z_nodes) == len_nodes


input_file = open(INPUT_FILENAME, 'r')
Lines = input_file.readlines()
INSTRUCTIONS = Lines[0][:-1]    # First line is instructions, and get rid of \n

Lines = Lines[2:]
MAPPING_DICT = create_node_mapping_dict(Lines)

nodes = get_list_of_starting_nodes(MAPPING_DICT)
num_steps = 0
len_instructions = len(INSTRUCTIONS)

while True:
    instr = INSTRUCTIONS[num_steps % len_instructions]
    for i, node in enumerate(nodes):
        branches = MAPPING_DICT[node]
        
        if instr == 'L':
            nodes[i] = branches[0]
        elif instr == 'R':
            nodes[i] = branches[1]

    num_steps += 1
    if goal_reached(nodes):
        break

print(num_steps)
