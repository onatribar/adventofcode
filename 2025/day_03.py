from aoc_lube import fetch, submit


def parse(text: str) -> list[str]:
    return text.strip().splitlines()

def max_joltage(row: str, k: int) -> int:
    indices = []
    length = len(row)

    for i in range(k):
        start = indices[-1] + 1 if indices else 0
        end = length - (k - i - 1)   # we must leave (k-i-1) chars after this pick

        # Find the max character and its earliest index in row[start:end]
        window = row[start:end]
        best = max(window)
        pos = window.index(best)     # earliest occurrence of max
        indices.append(start + pos)

    # Build final integer
    return int("".join(row[i] for i in indices))


def max_joltage_k(line: str, k: int = 12) -> int:
    n = len(line)
    i = 0
    picked: list[str] = []

    for to_pick in range(k, 0, -1):
        last_start = n - to_pick
        best_digit = "-1"
        best_pos = i

        for j in range(i, last_start + 1):
            d = line[j]
            if d > best_digit:
                best_digit = d
                best_pos = j
                if best_digit == "9":
                    break

        picked.append(best_digit)
        i = best_pos + 1

    return int("".join(picked))


def solution(text: str) -> tuple[int, int]:
    part1 =  sum(max_joltage(x, 2) for x in text)
    part2 = sum(max_joltage_k(x, 12) for x in text)
    return (part1, part2)

def main():
    text = fetch(2025, 3)
    lines = parse(text)

    p1, p2 = solution(lines)

    submit(2025, 3, 1, lambda: p1)
    submit(2025, 3, 2, lambda: p2)

if __name__ == "__main__":
    main()