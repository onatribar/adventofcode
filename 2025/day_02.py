from aoc_lube import fetch, submit


def parse(text: str) -> list[tuple[int, int]]:
    items = []
    for part in text.replace("\n", "").split(","):
        part = part.strip()
        if not part:
            continue
        start_str, end_str = part.split("-")
        items.append((int(start_str), int(end_str)))
    return items

def _part1_helper(num: int) -> bool:
    s = str(num)
    half = len(s) // 2
    return len(s) % 2 == 0 and s[:half] == s[half:]

def _part2_helper(num: int) -> bool:
    s = str(num)
    return s in (s + s)[1:-1]

def solution(ranges: tuple[int, int]) -> int:
    part1, part2 = 0, 0

    for start, end in ranges:
        part1 += sum(num for num in range(start, end + 1) if _part1_helper(num))
        part2 += sum(num for num in range(start, end + 1) if _part2_helper(num))

    return (part1, part2)

def main():
    text = fetch(2025, 2)
    ranges = parse(text)
    part1, part2 = solution(ranges)

    submit(2025, 2, 1, lambda: part1)
    submit(2025, 2, 2, lambda: part2)

if __name__ == "__main__":
    main()