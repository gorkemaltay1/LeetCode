class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s1 = s[:len(s)//2]
        s2 = s[len(s)//2:]
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        s1Count = 0
        s2Count = 0
        for i in vowels:
            s1Count += s1.count(i)
            s2Count += s2.count(i)
        return True if s1Count == s2Count else False