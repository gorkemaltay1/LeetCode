class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        sortedNums = sorted(nums)
        ans = 0
        for i in range(len(sortedNums)//2):
            ans = max(ans,sortedNums[i]+sortedNums[-i-1])
        return ans