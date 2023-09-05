class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        binX = bin(x).replace("0b", "")
        binY = bin(y).replace("0b", "")
        
        if len(binX) > len(binY):
            binY = ("0" * (len(binX) - len(binY))) + binY
        else:
            binX = ("0" * (len(binY) - len(binX))) + binX
        count = 0
        for i in range(len(binX)):
            if binX[i] != binY[i]:
                count += 1
            else:
                continue
        
        return count
        