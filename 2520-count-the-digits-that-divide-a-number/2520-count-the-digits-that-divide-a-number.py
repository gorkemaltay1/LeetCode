class Solution:
    def countDigits(self, num: int) -> int:
       divisors = (i for i in map(int, str(num)) if num % i == 0)
       return sum(1 for _ in divisors)