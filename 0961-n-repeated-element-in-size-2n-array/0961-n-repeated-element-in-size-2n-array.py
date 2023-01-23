class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        setNums = set(nums)
        for i in setNums:
            if nums.count(i) == len(nums)//2:
                return i