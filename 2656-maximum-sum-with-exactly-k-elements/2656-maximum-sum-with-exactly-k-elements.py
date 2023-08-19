class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        nums = list(sorted(nums))
        return int((k) * (nums[-1] + nums[-1] + k-1)/2) 
