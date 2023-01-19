class Solution:
    def pivotInteger(self, n: int) -> int:
        nList = [i for i in range(1,n+1)]
        for i in range(n//2,n):
            if sum(nList[:i+1]) == sum(nList[i:]):
                return i+1
        return -1