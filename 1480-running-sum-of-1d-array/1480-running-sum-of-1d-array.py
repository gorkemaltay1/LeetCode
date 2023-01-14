class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        cumsum = [nums[0]]
        for i in range(len(nums)-1):
            cumsum.append(nums[i+1]+cumsum[i])
        return cumsum