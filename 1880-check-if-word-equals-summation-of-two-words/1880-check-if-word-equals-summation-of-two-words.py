import string
class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        alphabet = list(string.ascii_lowercase)
        firstWordList = list()
        secondWordList =list()
        targetWordList = list()
        for i in firstWord:
            firstWordList.append(str(alphabet.index(i)))
        for i in secondWord:
            secondWordList.append(str(alphabet.index(i)))
        for i in targetWord:
            targetWordList.append(str(alphabet.index(i)))
            
        if int("".join(firstWordList)) + int("".join(secondWordList)) == int("".join(targetWordList)):
            return True
        return False