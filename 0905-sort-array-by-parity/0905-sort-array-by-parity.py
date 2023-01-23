class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        evenList = []
        oddList = []
        for i in nums:
            if i%2==0:
                evenList.append(i)
            else:
                oddList.append(i)
        return evenList + oddList