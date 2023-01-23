class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        li = list()
        for i in grid:
            li += i
        return len(list(filter(lambda x: (x < 0), li)))
        