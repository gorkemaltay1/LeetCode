from itertools import combinations

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        sortedNums = sorted(nums)
        return (sortedNums[-1] * sortedNums [-2]) - (sortedNums[0] * sortedNums[1])