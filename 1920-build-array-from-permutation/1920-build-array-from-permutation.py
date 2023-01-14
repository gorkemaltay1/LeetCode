class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        finalList = list()
        for i in range(len(nums)):
            finalList.append(nums[nums[i]])
        return finalList
            
        