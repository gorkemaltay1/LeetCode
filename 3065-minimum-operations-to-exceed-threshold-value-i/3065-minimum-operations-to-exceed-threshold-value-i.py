class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.append(k)
        nums = sorted(nums)
        return nums.index(k)