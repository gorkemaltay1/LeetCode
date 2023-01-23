class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        blankList = list()
        for i in nums:
            if i in blankList:
                return i
            else:
                blankList.append(i)