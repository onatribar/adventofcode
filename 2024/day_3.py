import aoc_lube

class Solution:
    def __init__(self) -> None:
        self.data:list[str] = aoc_lube.fetch(year=2024, day=3)

    def regex_matching(self, is_submissive=False) -> list[tuple[int,int]]:
        import re
        
        # part1
        if not is_submissive:
            pattern_mul:str = r"mul\s*\(\s*(\d+)\s*,\s*(\d+)\s*\)"
            matches:list[tuple[str, str]] = re.findall(pattern_mul, self.data)
            return [(int(x), int(y)) for x, y in matches]

        # part 2
        pattern_all:str = r"((?:mul\s*\(\s*(\d+)\s*,\s*(\d+)\s*\))|(?:do\s*\(\s*\))|(?:don't\s*\(\s*\)))"
        matches = re.finditer(pattern_all, self.data)

        result:list[tuple[int,int]] = []
        ignore:bool = False

        for match in matches:
            if match.group() == "don't()":
                ignore = True
            elif match.group() == "do()":
                ignore = False
            elif not ignore and match.group(2) and match.group(3):
                result.append((int(match.group(2)), int(match.group(3))))
        return result

    def sol1(self) -> int:
        return sum(x * y for x,y in self.regex_matching())

    def sol2(self) -> int:
        return sum(x * y for x,y in self.regex_matching(is_submissive=True))

if __name__ == "__main__":
    ans = Solution()
    aoc_lube.submit(year=2024, day=3, part=1, solution=ans.sol1)
    aoc_lube.submit(year=2024, day=3, part=2, solution=ans.sol2)
    del(ans)