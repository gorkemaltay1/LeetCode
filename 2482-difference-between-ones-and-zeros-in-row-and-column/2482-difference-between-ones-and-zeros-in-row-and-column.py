class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        onesRow = []
        onesCol = []
        zerosRow = []
        zerosCol = []
        
        #Creating diff-zeros matrix
        diff = [[0 for x in range(len(grid[0]))] for x in range(len(grid))] 
            
        #Counting ones and zeros
        for i in grid:
            onesRow.append(i.count(1))
            zerosRow.append(i.count(0))
            
        for i in range(len(grid[0])):
            countOnesCol = 0
            countZerosCol = 0
            for j in grid:
                if j[i] == 1:
                    countOnesCol += 1
                else:
                    countZerosCol += 1
            onesCol.append(countOnesCol)
            zerosCol.append(countZerosCol)
        
        #Preparing the diff matrix
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                diff[i][j] = onesRow[i] + onesCol[j] - zerosRow[i] - zerosCol[j]
        
        return diff
        
                