class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        matrix = [[0 for _ in range(n)] for i in range(m)]
        for i in indices:
            for j in range(n):
                matrix[i[0]][j] += 1
            for k in range(m):
                matrix[k][i[1]] += 1
        count = 0
        for i in matrix:
            count += len(list(filter(lambda x: (x%2 != 0) , i)))
        return count