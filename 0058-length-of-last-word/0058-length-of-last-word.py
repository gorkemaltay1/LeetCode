class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        listed = s.split()
        return len(listed[-1])
