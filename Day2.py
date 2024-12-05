import numpy as np

from aoc_helpers import parse_input

# Get Input
lines = parse_input(2)


# Functions
def safe(list):

    bad = 0
    pos_count = sum([i > 0 for i in list])
    zero_count = sum([i == 0 for i in list])
    for x in list:
        if abs(x) > 3:
            bad += 1
        elif abs(x) == 0:
            bad += 1
        elif x > 0 and pos_count <= (len(list)-zero_count)/2:
            bad += 1
        elif x < 0 and pos_count >= (len(list)-zero_count)/2:
            bad += 1

    if bad > 0:
        return False
    return True


# Part 1
seqs = [[int(x) for x in line.split()] for line in lines]
safe_lists = [safe(np.diff(seq)) for seq in seqs]
print(sum(safe_lists))

# Part 2
safe_count = 0
for seq in seqs:
    if safe(np.diff(seq)):
        safe_count += 1
    else:
        for i in range(len(seq)):
            new_seq = seq[:i] + seq[i+1:]
            if safe(np.diff(new_seq)):
                safe_count += 1
                break
print(safe_count)
