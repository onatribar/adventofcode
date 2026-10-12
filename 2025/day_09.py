import aoc_lube
from itertools import combinations

RAW = aoc_lube.fetch(year=2025, day=9)

def parse_raw(raw: str) -> tuple[tuple[int, int], ...]:
    return tuple(tuple(map(int, line.split(","))) for line in raw.splitlines())

DATA = parse_raw(RAW)

def part_one():
    return max(
        (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1 )
        for (p1, p2) in combinations(DATA, 2)
    )

def part_two():
    pass

aoc_lube.submit(year=2025, day=9, part=1, solution=part_one)
aoc_lube.submit(year=2025, day=9, part=2, solution=part_two)
