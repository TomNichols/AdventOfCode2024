import time
import multiprocessing

from aoc_helpers import parse_input


class Guard:
    def __init__(self, input):
        self.position = self.locate(input)
        self.orientation = "up"
        self.path = [self.position]
        self.orientations = [self.orientation]

    def locate(self, input):
        y = 0
        for line in input:
            x = 0
            for char in line:
                if char == "^":
                    return [x, y]
                x += 1
            y += 1

    def reorient(self):
        map = {"up": "right", "right": "down", "down": "left", "left": "up"}
        return map[self.orientation]

    def unobstructed(self, new_position, obstacles):
        if new_position in obstacles:
            return False
        else:
            return True

    def get_next_position(self):
        if self.orientation == "up":
            return [self.position[0], self.position[1] - 1]
        elif self.orientation == "right":
            return [self.position[0] + 1, self.position[1]]
        elif self.orientation == "down":
            return [self.position[0], self.position[1] + 1]
        elif self.orientation == "left":
            return [self.position[0] - 1, self.position[1]]

    def move(self, obstacles):
        new_position = self.get_next_position()

        # Throw an error if we're about to get stuck in a loop
        if new_position in self.path:
            ids = [i for i, j in enumerate(self.path) if j == new_position]
            orientations = [self.orientations[i] for i in ids]
            if self.orientation in orientations:
                raise Exception("Stuck in loop")

        # Moving along path if unobstructed, turning if not
        if self.unobstructed(new_position, obstacles):
            self.position = new_position
            self.path += [new_position]
            self.orientations += [self.orientation]
        else: 
            self.orientation = self.reorient()


class Lab:
    def __init__(self, input):
        self.height = len(input)
        self.width = len(input[0])
        self.obstacles = self.find_obstacles(input)

    def find_obstacles(self, input):
        y = 0
        obstacles = []
        for line in input:
            x = 0
            for char in line:
                if char == "#":
                    obstacles += [[x, y]]
                x += 1
            y += 1
        return obstacles

    def in_bounds(self, guard: Guard):
        if guard.position[0] <= 0 or guard.position[0] >= self.width - 1:
            return False
        if guard.position[1] <= 0 or guard.position[1] >= self.height - 1:
            return False
        else:
            return True

    def draw_path(self, guard: Guard):
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                if [x, y] in self.obstacles:
                    row += "#"
                elif [x, y] in guard.path:
                    row += "x"
                else:
                    row += "."
            print(row)


# Part 1
input = parse_input(6)
lab = Lab(input)
guard = Guard(input)
i = 0
start = time.time()
while lab.in_bounds(guard):
    guard.move(lab.obstacles)
unique_path_locs = [[int(s.split("-")[0]), int(s.split("-")[1])] for s in list(set(([str(loc[0])+"-"+str(loc[1]) for loc in guard.path])))]
#print(unique_path_locs)
print(len(unique_path_locs))
print(time.time() - start)


# Part 2
# Tried doing it properly by extending 1 but couldn't work out logic
# So here is a brute-force approach to finding loops
def f(loc):

    lab = Lab(input)
    guard = Guard(input)
    lab.obstacles += [loc]

    # While loop
    try:
        while lab.in_bounds(guard):
            guard.move(lab.obstacles)
        return 0
    except:
        return 1

t_start = time.time()
with multiprocessing.Pool(processes=20) as pool:
    outputs = pool.map(f, unique_path_locs)
print(sum(outputs))
print(time.time() - t_start)