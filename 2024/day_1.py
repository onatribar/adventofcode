import aoc_lube

class Solution:
    def __init__(self) -> None:
        self.data:list = aoc_lube.fetch(year=2024, day=1).split("\n")

        self.col1:list = []
        self.col2:list = []

        for line in self.data:
            row_values:list = line.split()
            if len(row_values) == 2:
                self.col1.append(row_values[0])
                self.col2.append(row_values[1])

        if len(self.col1) != len(self.col2):
            raise Exception("Data not in correct format!")

    def sort(self) -> None:
        self.col1.sort()
        self.col2.sort()

    def sol1(self) -> int:
        total_distance:int = 0
        self.sort()
        for i in range(len(self.col1)):
            total_distance += abs( int(self.col1[i]) - int(self.col2[i]) )
        return total_distance
    
    def sol2(self) -> int:
        hash_map:dict = {}
        similarity_score:int = 0
        # find frequencies
        for item in self.col2:
            if item not in hash_map:
                hash_map[item] = 1
            else:
                hash_map[item] += 1
        # sum the stuff
        similarity_score += sum( int(item) * int(hash_map[item]) for item in self.col1 if item in hash_map )
        return similarity_score

if __name__ == "__main__":
    soln = Solution()
    aoc_lube.submit(year=2024, day=1, part=1, solution=soln.sol1)
    aoc_lube.submit(year=2024, day=1, part=2, solution=soln.sol2)
    del(soln)