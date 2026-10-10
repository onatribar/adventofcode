import aoc_lube

RAW = aoc_lube.fetch(year=2025, day=7)

def parse_raw(text: str) -> list[str]:
    return text.splitlines()

DATA = parse_raw(RAW)

def part_one():
    pos: list[bool] = [False] * len(DATA[0])
    pos[DATA[0].index("S")] = True

    split_count: int = 0
    
    for line in DATA:
        hat_locations: list[int] = [i for i, char in enumerate(line) if char == "^" and pos[i]]
        for hat_idx in hat_locations:
            pos[hat_idx] = False
            if hat_idx + 1 < len(pos):
                pos[hat_idx + 1] = True
            if hat_idx > 0:
                pos[hat_idx - 1] = True
            split_count += 1

    return split_count

def part_two():
    from functools import cache
    rows, cols = len(DATA), len(DATA[0])

    @cache
    def dfs(row: int, col: int) -> int:
        if row == rows: # basecase. beam fell off the bottom, one complete timeline
            return 1
        if DATA[row][col] == "^": # splitter creates a multiverse
            total = 0
            if col > 0:
                total += dfs(row + 1, col - 1)
            if col + 1 < cols:
                total += dfs(row + 1, col + 1)
            return total
        return dfs(row + 1, col)  # no splitter atm, so it keep falling

    start = DATA[0].index("S")
    return dfs(0, start)

aoc_lube.submit(year=2025, day=7, part=1, solution=part_one)
aoc_lube.submit(year=2025, day=7, part=2, solution=part_two)
