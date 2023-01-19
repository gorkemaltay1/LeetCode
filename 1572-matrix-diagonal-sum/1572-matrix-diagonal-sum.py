class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        primaryDiagonal = 0
        secondaryDiagonal = 0
        for i in range(len(mat)):
            primaryDiagonal += mat[i][i]
            secondaryDiagonal += mat[-i-1][i]
        if len(mat)%2 == 0:
            return primaryDiagonal + secondaryDiagonal
        return primaryDiagonal + secondaryDiagonal - mat[len(mat)//2][len(mat)//2]
        