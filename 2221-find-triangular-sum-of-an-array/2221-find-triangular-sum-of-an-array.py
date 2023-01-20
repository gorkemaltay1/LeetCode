class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        tempList = nums
        for i in range(len(nums),1,-1):
            tempTempList = [(tempList[j]+tempList[j+1])%10 for j in range(i-1)]
            tempList = tempTempList
        return tempList[0]
            
        