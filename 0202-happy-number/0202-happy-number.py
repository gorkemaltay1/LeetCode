class Solution:
    def isHappy(self, n: int) -> bool:
        calcd = set()
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n in calcd:
                return False
            else:
                calcd.add(n)
        return True