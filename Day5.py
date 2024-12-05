from functools import cmp_to_key

from aoc_helpers import parse_input

# Get Input
rules = parse_input("5p1")
updates = parse_input("5p2")

# Part 1
count = 0
incorrect_update_ids = []
update_id = 0
for update in updates:
    pages = update.split(",")
    for i in range(len(pages)-1):
        if pages[i] + "|" + pages[i+1] in rules:
            if i == len(pages) - 2:
                count += int(pages[len(pages)//2])
            pass
        else:
            incorrect_update_ids += [update_id]
            break
    update_id += 1
print(count)

# Part 2
incorrect_updates = [updates[i] for i in incorrect_update_ids]
count = 0
for update in incorrect_updates:
    pages = update.split(",")
    pages = sorted(pages, key=cmp_to_key(lambda x, y: -1 if x + "|" + y in rules else 1))
    count += int(pages[len(pages)//2])

print(count)
