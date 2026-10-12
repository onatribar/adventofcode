import aoc_lube
from collections import Counter
from itertools import combinations
from math import prod
from typing import Final, NamedTuple, TypeAlias

class Box(NamedTuple):
    x: int
    y: int
    z: int

Pair: TypeAlias = tuple[int, int, int]  # (squared dist., index i, index j)

RAW = aoc_lube.fetch(year=2025, day=8)

def parse_raw(raw: str) -> list[Box]:
    return [Box(*map(int, line.split(","))) for line in raw.splitlines()]

DATA = parse_raw(RAW)

def squared_dist(a: Box, b: Box) -> int:  # sqrt / euclidian dist. isn't necessary
    return (a.x - b.x) ** 2 + (a.y - b.y) ** 2 + (a.z - b.z) ** 2

PAIRS: Final[list[Pair]] = sorted(
    (squared_dist(DATA[i], DATA[j]), i, j)
    for i, j in combinations(range(len(DATA)), 2)
)

def find(parent: list[int], i: int) -> int:
    while parent[i] != i:
        parent[i] = parent[parent[i]]
        i = parent[i]
    return i

def part_one() -> int:
    parent: list[int] = list(range(len(DATA)))
    for _, i, j in PAIRS[:1000]: # shortest 1k distances
        root_i: int = find(parent, i)
        root_j: int = find(parent, j)
        if root_i != root_j:
            parent[root_i] = root_j

    sizes: Counter[int] = Counter(find(parent, i) for i in range(len(DATA)))
    return prod(size for _, size in sizes.most_common(3))

def part_two() -> int:
    parent: list[int] = list(range(len(DATA)))
    merges: int = 0
    for _, i, j in PAIRS:
        root_i: int = find(parent, i)
        root_j: int = find(parent, j)
        if root_i != root_j:
            parent[root_i] = root_j
            merges += 1
            if merges == len(DATA) - 1:
                return DATA[i].x * DATA[j].x
    raise ValueError("Boxes didn't merge a single circuit!")

aoc_lube.submit(year=2025, day=8, part=1, solution=part_one)
aoc_lube.submit(year=2025, day=8, part=2, solution=part_two)