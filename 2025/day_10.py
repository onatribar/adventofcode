import aoc_lube

RAW = aoc_lube.fetch(year=2025, day=10)

def parse_raw():
    formatted_data = []

    for line in RAW.splitlines():
        items = line.split()

        lights = [x == "#" for x in items[0][1:-1]]
        buttons = [[int(x) for x in button[1:-1].split(",")] for button in items[1:-1]]
        jolts = [int(x) for x in items[-1][1:-1].split(",")]

        formatted_data.append((lights, buttons, jolts))

    return formatted_data

"""
    DATA[i][0] := indicator light diagrams — list[bool]
    DATA[i][1] := wiring schematics        — list[list[int]]
    DATA[i][2] := joltage requirements     — list[int]
"""
DATA = parse_raw()

def apply_button(lights, button):
    lights_copy = lights.copy()
    for b in button:
        lights_copy[b] = not lights_copy[b]
    return lights_copy

# exhaustive search, O(2^n)
def part_one():
    def solve(val, lights, buttons):
        if not any(lights): # lights are off, one soln. produced
            return val
        if len(buttons) == 0: # sequence didn't produce a soln.
            return float('inf')
        step1 = solve(val + 1, apply_button(lights, buttons[0]), buttons[1:])
        step2 = solve(val, lights, buttons[1:])
        return min(step1, step2)

    return sum(solve(0, lights, buttons) for lights, buttons, _ in DATA)

def part_two():
    pass

aoc_lube.submit(year=2025, day=10, part=1, solution=part_one)
aoc_lube.submit(year=2025, day=10, part=2, solution=part_two)
