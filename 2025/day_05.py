import aoc_lube

RAW = aoc_lube.fetch(year=2025, day=5)

# output: [(range_start, range_end)] sorted by start, {item_id}
def parse_raw(text: str) -> tuple[list[tuple[int, int]], set[int]]:
    the_great_divide = text.split("\n\n")
    ranges, items = set(), set()
    for line in the_great_divide[0].strip().splitlines():
        low, high = line.split("-")
        ranges.add((int(low), int(high)))
    for item in the_great_divide[1].strip().splitlines():
        items.add(int(item))
    return (sorted(ranges, key=lambda x: x[0]), items)
     
RANGES, INGREDIENTS = parse_raw(RAW)

def part_one():
    return sum(any(low <= x <= high for low, high in RANGES) for x in INGREDIENTS)

# merge intervals problem
def part_two():
    merged = []
    cur_low, cur_high = RANGES[0]

    for low, high in RANGES[1:]:
        if low > cur_high:
            merged.append((cur_low, cur_high))
            cur_low, cur_high = low, high
        else:
            cur_high = max(cur_high, high)

    merged.append((cur_low, cur_high))
    return sum(high - low + 1 for low, high in merged)

aoc_lube.submit(year=2025, day=5, part=1, solution=part_one)
aoc_lube.submit(year=2025, day=5, part=2, solution=part_two)
