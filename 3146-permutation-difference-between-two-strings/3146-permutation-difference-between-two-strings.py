class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        sList = list(s)
        tList = list(t)
        
        summ = 0
        for i in sList:
            summ+=abs(sList.index(i) - tList.index(i))
            
        return summ