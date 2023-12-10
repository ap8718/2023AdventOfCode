INPUT_FILENAME = "day5_input.txt"

SEED_TO_SOIL_DELTA = dict({})
SOIL_TO_FERTILIZER_DELTA = dict({})
FERTILIZER_TO_WATER_DELTA = dict({})
WATER_TO_LIGHT_DELTA = dict({})
LIGHT_TO_TEMPERATURE_DELTA = dict({})
TEMPERATURE_TO_HUMIDITY_DELTA = dict({})
HUMIDITY_TO_LOCATION_DELTA = dict({})

def get_seeds(Lines):
    seeds_string = Lines[0]
    seeds = seeds_string.split(':')[1]
    seeds = seeds.split(' ')
    return [int(s) for s in seeds if s != '']



input_file = open(INPUT_FILENAME, 'r')
Lines = input_file.readlines()

seeds = get_seeds(Lines)
print(seeds)
