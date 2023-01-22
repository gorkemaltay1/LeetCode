class Solution:
    def sumZero(self, n: int) -> List[int]:
        finalList = [i for i in range(1,n)]
        finalList.append(0-sum(finalList))
        return finalList
        
        