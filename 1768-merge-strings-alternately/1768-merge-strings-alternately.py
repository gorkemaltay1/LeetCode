class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        k = len(word2)
        s = ""
        for i in range(min(n,k)):
            s += word1[i] + word2[i]
        if n==k:
            return s
        elif n<k:
            return s + word2[n-k:]
        else:
            return s + word1[k-n:]
            