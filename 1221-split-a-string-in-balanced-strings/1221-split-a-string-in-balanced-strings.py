class Solution:
    def balancedStringSplit(self, s: str) -> int:
        countR = 0
        countL = 0
        substrCnt = 0
        for i in s:
            if i == "R":
                countR += 1
            elif i == "L":
                countL += 1
            
            if countR == countL:
                substrCnt += 1
        
        return substrCnt