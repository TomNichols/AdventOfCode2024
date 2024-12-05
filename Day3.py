from re import finditer

# Get Input
string = open("Day3.txt").read()


# Function
def regex_matches(string, pattern):
    matches = []
    for match in finditer(pattern, string):
        matches += [{"span": match.span(), "group": match.group()}]
    return matches


# Part 1
total = 0
mul_locs = []
matches = regex_matches(string, r'mul\(\d+,\d+\)')
for match in matches:
    pair = match["group"].split("(")[1].split(")")[0].split(",")
    total += int(pair[0])*int(pair[1])
    mul_locs += [match["group"][0]]
print(total)

# Part 2
matches = []
total = 0
for s in string.split("do()"):
    matches += regex_matches(s.split("don't()")[0], r'mul\(\d+,\d+\)')
for match in matches:
    pair = match["group"].split("(")[1].split(")")[0].split(",")
    total += int(pair[0])*int(pair[1])
    mul_locs += [match["group"][0]]
print(total)
