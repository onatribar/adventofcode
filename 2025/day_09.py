import aoc_lube
from itertools import combinations

RAW = aoc_lube.fetch(year=2025, day=9)

def parse_raw(raw: str) -> tuple[tuple[int, int], ...]:
    return tuple(tuple(map(int, line.split(","))) for line in raw.splitlines())

POINTS = parse_raw(RAW)
EDGES = list(zip(POINTS, POINTS[1:] + POINTS[:1]))

def get_rectangle_area(p1: tuple[int,int], p2: tuple[int,int]) -> int:
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1 )

def part_one():
    return max(
        get_rectangle_area(p1, p2)
        for (p1, p2) in combinations(POINTS, 2)
    )

def part_two():
    def is_inside(x, y) -> bool:
        # even-odd theorem, ray casting to the right
        flag: bool = False
        for (x1, y1), (x2, y2) in EDGES:
            if x1 == x2 and x1 > x and min(y1, y2) < y < max(y1, y2):
                flag = not flag
        return flag

    def edge_cuts_interior(left: int, right: int, top: int, bottom: int) -> bool:
        # if a boundary line passes through the rectangle, part of it is outside
        for (x1, y1), (x2, y2) in EDGES:
            edge_left, edge_right = sorted((x1, x2))
            edge_top, edge_bottom = sorted((y1, y2))

            overlap_horizontal: bool = edge_left < right and edge_right > left
            overlap_vertical: bool = edge_top < bottom and edge_bottom > top

            if overlap_horizontal and overlap_vertical:
                return True
        return False

    # check rectangles in descending area so we know the first valid one is the answer
    corner_pairs = sorted(
        combinations(POINTS, 2),
        key=lambda pair: get_rectangle_area(*pair),
        reverse=True,
    )

    for p1, p2 in corner_pairs:
        left, right = sorted((p1[0], p2[0]))
        top, bottom = sorted((p1[1], p2[1]))

        if left == right or top == bottom:
            continue
        if edge_cuts_interior(left, right, top, bottom):
            continue
        # no edge crosses it, so it's entirely inside or entirely outside
        if is_inside(left + 0.5, top + 0.5): # padding so the ray doesnt go through a vertex
            return get_rectangle_area(p1, p2)

    raise ValueError("We ran out of red tiles")

aoc_lube.submit(year=2025, day=9, part=1, solution=part_one)
aoc_lube.submit(year=2025, day=9, part=2, solution=part_two)
