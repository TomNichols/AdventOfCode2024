from aoc_helpers import parse_input

# Get Input
lines = parse_input(1)

# Part 1
left = sorted([int(line.split()[0]) for line in lines])
right = sorted([int(line.split()[1]) for line in lines])
distance = [abs(left[i] - right[i]) for i in range(len(left))]
print(sum(distance))

# Part 2
print(sum([l*right.count(l) for l in left]))