class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums = sorted(nums)
        if nums[-1] % nums[0] == 0:
            return nums[0]
        
        gcd = 1
        for i in range(1,nums[0]//2+1):
            if nums[-1] % i == 0 and nums[0] % i == 0:
                gcd = i
        return gcd