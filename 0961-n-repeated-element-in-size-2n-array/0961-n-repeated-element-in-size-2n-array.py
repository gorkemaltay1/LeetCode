class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        setNums = set(nums)
        length = len(nums)//2
        for i in setNums:
            if nums.count(i) == length:
                return i