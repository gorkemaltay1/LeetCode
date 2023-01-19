class Solution:
    def replaceDigits(self, s: str) -> str:
        listS = [*s]
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for i in range(0,len(listS)-1,2):
            listS[i+1] = alphabet[alphabet.index(listS[i])+int(listS[i+1])]
        return "".join(listS)