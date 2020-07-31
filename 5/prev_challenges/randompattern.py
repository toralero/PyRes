import random

# 0 – green square
# 1 – red triangle
# 2 – yellow circle
# 3 – blue star
symbols = [0, 1, 2, 3]

# Sequence that is going to be matched
sequence = [3,2,2]

# Set random seed so that "random" will always produce
# the same result
random.seed(22041997)

# How many rows?
row_len = 100
# How many columns?
column_len = 20

pattern = []

# Function used for printing a pattern
def print_pattern(pattern):
    for row in pattern:
        print(row)

# Creating the pattern
for i in range(row_len):
    row = []
    for j in range(column_len):
        row.append(random.randint(0,3))
    pattern.append(row)

print_pattern(pattern)

# Function for detecting a sequence in the pattern
def pattern_match(sequence, pattern):
    count = 0
    next_symbol = [0] * len(symbols)
    coord_list = []
    for x in range(0, len(pattern)):
        if len(sequence) <= len(pattern[x]):
            for y in range(0, len(pattern[x]) - len(sequence)-1):
                if (pattern[x][y:y+len(sequence)] == sequence):
                    # PATTERN FOUND
                    coord = (x,y)
                    coord_list.append(coord)
                    count += 1
                    column_end = y+len(sequence)-1
                    if column_end < len(pattern[x])-1:
                        next_symbol[pattern[x][column_end+1]] += 1
    return count, coord_list,  next_symbol

count, coord_list,  next_symbol = pattern_match(sequence, pattern)

print(count)
print_pattern(coord_list)
print(next_symbol)

def decide_recommendation(next_symbol_list):
    index_max = max(range(len(next_symbol_list)), key = next_symbol_list.__getitem__)
    if index_max == 0:
        print("I would recommend the green square!")
    elif index_max == 1:
        print("I would recommend the red triangle!")
    elif index_max == 2:
        print("I would recommend the yellow circle!")
    elif index_max == 3:
        print("I would recommend the blue star!")
    else:
        print("Not really sure what to recommend...")

decide_recommendation(next_symbol)
