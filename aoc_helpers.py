
def parse_input(day):
    path = f"Day{day}.txt"
    with open(path) as file:
        lines = [line.rstrip() for line in file]
    return lines

def parse_input_as_string(day):
    path = f"Day{day}.txt"
    with open(path) as file:
        return str(file)