from aoc_lube import fetch, submit

def parse(text: str) -> list[tuple[str, int]]:
    return [((line[0], int(line[1:]))) for line in text.strip().splitlines()]


def solve(moves: list[tuple[str, int]]) -> tuple[int, int]:
    pos = 50
    part1, part2 = 0, 0

    for direction, dist in moves:
        step = -1 if direction == "L" else 1

        # part 2: count every click landing on 0
        for _ in range(dist):
            pos = (pos + step) % 100
            if pos == 0:
                part2 += 1

        # part 1: count only iff final resting position == 0
        if pos == 0:
            part1 += 1

    return part1, part2


def main():
    text = fetch(2025, 1)
    moves = parse(text)
    p1, p2 = solve(moves)

    submit(2025, 1, 1, lambda: p1)
    submit(2025, 1, 2, lambda: p2)

if __name__ == "__main__":
    main()
    