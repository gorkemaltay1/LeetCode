class Solution:
    def repeatedCharacter(self, s: str) -> str:
        letterDict = dict()
        for i in set([*s]):
            letterDict[i] = 0
        
        for i in s:
            letterDict[i] += 1
            if letterDict[i] == 2:
                return i