class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elementSum = sum(nums)
        digitSum = 0
        for i in nums:
            a = str(i)
            for i in range(len(a)):
                digitSum += int(a[i])
            
        return abs(elementSum - digitSum)
        