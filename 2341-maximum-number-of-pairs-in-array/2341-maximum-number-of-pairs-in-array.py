class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        numbers = list(set(nums))
        lenOfNums = len(nums)
        pair = 0
        for i in numbers:
            if nums.count(i)%2 == 0:
                pair += nums.count(i)//2
                lenOfNums -= nums.count(i)
            else:
                pair += nums.count(i)//2
                lenOfNums -= nums.count(i)-1
        return [pair,lenOfNums]
            