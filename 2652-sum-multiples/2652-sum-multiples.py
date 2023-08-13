class Solution:
    def sumOfMultiples(self, n: int) -> int:
        nums = list()
        for i in range(n+1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
               nums.append(i)
        return sum(nums)