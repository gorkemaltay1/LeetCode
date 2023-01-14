class Solution:
    def minimumSum(self, num: int) -> int:
        x = str(num)
        araba = [int(i) for i in x]
        newList = sorted(araba)
        return newList[0]*10 + newList[1]*10 +newList[2]+newList[3]
             