class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        firstLetters = ""
        for i in words:
            firstLetters += i[0]
        
        if firstLetters == s:
            return True
        return False