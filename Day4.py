import re

from aoc_helpers import parse_input

# Get Input
x_lines = parse_input(4)

# Get vertical lines
height = len(x_lines)
width = len(x_lines[0])
y_lines = [''.join(line[i] for line in x_lines) for i in range(width)]

# Get diagonal lines
d_lines_tr = [''.join(x_lines[i - k][width - 1 - k] for k in range(max(0, i - height + 1), min(i + 1, width))) for i in range(height + width - 1)]
d_lines_tl = [''.join(x_lines[i - k][k] for k in range(max(0, i - height + 1), min(i + 1, width))) for i in range(height + width - 1)]

# Part 1
match_strings = ["XMAS", "SAMX"]
all_lines = x_lines + y_lines + d_lines_tr + d_lines_tl
count = sum([sum([line.count(match) for match in match_strings]) for line in all_lines])
print(count)


# Part 2
def is_in_bounds(x, y, w, h):
    if x == 0 or x == w-1:
        return False
    elif y == 0 or y == h-1:
        return False
    else:
        return True


y, count = 0, 0
match_strings = ["MAS", "SAM"]
for line in x_lines:
    x = 0
    for char in line:
        if char == "A" and is_in_bounds(x, y, width, height):
            diag_1 = x_lines[y-1][x-1] + "A" + x_lines[y+1][x+1]
            diag_2 = x_lines[y-1][x+1] + "A" + x_lines[y+1][x-1]
            if diag_2 in match_strings and diag_1 in match_strings:
                count += 1
        x += 1
    y += 1
print(count)
