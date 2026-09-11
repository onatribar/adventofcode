import aoc_lube
import math

RAW = aoc_lube.fetch(year=2025, day=6)

# example: (['24 ', '67 ', '619'], '*')
# each str is padded to problem width s.t. n[i] is always column i (will help w/ p2)
def parse_raw(text: str) -> list[tuple[list[str], str]]:
    lines = text.rstrip("\n").split("\n")
    width = max(len(line) for line in lines)
    lines = [line.ljust(width) for line in lines]

    problems = []
    start = 0
    for i in range(width + 1):
        if i == width or all(line[i] == " " for line in lines):
            if i > start:
                chunk = [line[start:i] for line in lines]
                problems.append((chunk[:-1], chunk[-1].strip()))
            start = i + 1
    return problems

DATA = parse_raw(RAW)

def calculate(nums: list[int], symbol: str) -> int:
    if symbol == "+":
        return sum(nums)
    elif symbol == "*":
        return math.prod(nums)
    raise Exception("HOW DID WE GET HERE?! ♬ ♪ ٩(ˊᗜˋ*)و")

def part_one():
    return sum(calculate([int(n) for n in nums], symbol) for nums, symbol in DATA)

def part_two():
    res = 0
    for nums, symbol in DATA:
        new_nums = []
        # transpose, read each character column top to bottom
        for i in range(len(nums[0])):
            new_nums.append(int("".join(n[i] for n in nums)))
        res += calculate(new_nums, symbol)
    return res

aoc_lube.submit(year=2025, day=6, part=1, solution=part_one)
aoc_lube.submit(year=2025, day=6, part=2, solution=part_two)
