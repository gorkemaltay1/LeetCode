class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        result = []
        for i in range(len(grid)-2):
            maxedVal = []
            for j in range(len(grid)-2):
                maxInMatrix = max(grid[i][j:j+3]+grid[i+1][j:j+3]+grid[i+2][j:j+3])
                maxedVal.append(maxInMatrix)
            result.append(maxedVal)
        return result
            
        