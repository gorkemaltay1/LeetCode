class Solution:
    def isPalindrome(self, s: str) -> bool:
        empStr = ""
        for i in s:
            if (ord(i) >= 48 and ord(i) < 58) or (ord(i) >= 65 and ord(i) < 91) or (ord(i) >= 97 and ord(i) < 123):
                empStr += i
        empStr = empStr.lower()
        lenstr = len(empStr)
        if empStr == empStr[::-1]:
            return True
        return False