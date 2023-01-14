class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        numList = [int(x) for x in str(n)]
        prodResult = 1
        for i in range(len(numList)):
            prodResult *= numList[i]
        sumResult = sum(numList)
        return prodResult - sumResult