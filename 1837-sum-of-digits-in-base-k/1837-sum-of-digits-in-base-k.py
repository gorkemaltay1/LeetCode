class Solution:
    def sumBase(self, n: int, k: int) -> int:
        digits = []
        while n > 0:
            digit = n%k
            digits.append(digit)
            n //= k
        return sum(digits)