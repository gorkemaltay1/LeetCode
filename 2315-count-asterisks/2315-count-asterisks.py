class Solution:
    def countAsterisks(self, s: str) -> int:
        wordList = s.split("|")
        count = 0
        for i in range(0,len(wordList),2):
            count += wordList[i].count("*")
        
        return count
        
        