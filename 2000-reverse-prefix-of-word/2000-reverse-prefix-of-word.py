class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        letterList = [*word]
        finalList = []
        try:
            finalList = letterList[letterList.index(ch)::-1] + letterList[letterList.index(ch)+1:]
            return "".join(finalList)
        except:
            return word