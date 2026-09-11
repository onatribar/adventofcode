import aoc_lube

RAW = aoc_lube.fetch(2025, 4)

def parse_raw(text: str) -> list[str]:
    return {
        (row, col)
        for row, line in enumerate(text.strip().splitlines())
        for col, char in enumerate(line)
        if char == "@"
    }

DATA = parse_raw(RAW)

NEIGHBOURS = tuple(
    # all cardinal & diagonal dirs
    (d_row, d_col) 
    for d_row in (-1, 0, 1) 
    for d_col in (-1, 0, 1) 
    if (d_row, d_col) != (0, 0)
)

def count_neighbours( rolls: set[tuple[int,int]], row: int, col: int ) -> int:
    return sum((row + d_row, col + d_col) in rolls for d_row, d_col in NEIGHBOURS)

def part_one() -> int:
    return sum(count_neighbours(DATA, row, col) < 4 for row, col in DATA)
            
def part_two() -> int:
    rolls, removed = DATA, 0

    while True:
        accessible = {x for x in rolls if count_neighbours(rolls, *x) < 4}
        if not accessible: return removed
        rolls -= accessible
        removed += len(accessible)

aoc_lube.submit(year=2025, day=4, part=1, solution=part_one)
aoc_lube.submit(year=2025, day=4, part=2, solution=part_two)
