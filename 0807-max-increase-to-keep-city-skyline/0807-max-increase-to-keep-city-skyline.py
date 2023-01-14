class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        summation = 0
        for i in range(len(grid)):
            westOrEast = max(grid[i])
            for j in range(len(grid)):
                northOrSouth = max([row[j] for row in grid])
                summation +=  min(westOrEast,northOrSouth) - grid[i][j]
        return summation