class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        letters = list(set([*s]))
        lastOccurence = s.count(letters[0])
        for i in letters:
            if s.count(i) != lastOccurence:
                return False
        return True