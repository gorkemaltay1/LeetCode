class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        wordList = s.split(" ")
        return " ".join(wordList[:k])
        