class Solution:
    def countBits(self, n: int) -> List[int]:
        finalList = []
        for i in range(n+1):
            finalList.append(bin(i).count("1"))
        return finalList
                