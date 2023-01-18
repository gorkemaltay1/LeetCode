class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowedList = sorted(set([*allowed]))
        count = 0
        for i in words:
            for j in sorted(set([*i])):
                if j not in allowedList:
                    break
                if j == sorted(set([*i]))[-1] and j in allowedList:
                    count +=1
                
            
        return count