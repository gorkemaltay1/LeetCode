class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        sortedNums = sorted(nums)
        pairs = set()
        for i in range(len(sortedNums)//2):
            pairs.add((sortedNums[i],sortedNums[-i-1]))
        maxSum = 0
        for j in pairs:
            if sum(j) > maxSum:
                maxSum = sum(j)
        return maxSum
            