class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        finalList = []
        initial = 0
        for i in s:
            if i == "I":
                finalList.append(initial)
                initial += 1
            else:
                finalList.append(n)
                n-=1
        finalList.append(n)
        return finalList