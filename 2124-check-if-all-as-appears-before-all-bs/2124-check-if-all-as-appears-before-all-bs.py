class Solution:
    def checkString(self, s: str) -> bool:
        aIndex = s.rindex("a") if "a" in s else -1
        bIndex = s.index("b") if "b" in s else -1
        if bIndex > aIndex or aIndex == -1 or bIndex == -1:
            return True
        return False
        