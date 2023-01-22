class Solution:
    def findGCD(self, nums: List[int]) -> int:
        #By using Euclidean Algorithm..
        n,k = min(nums),max(nums)
        while n:
            n,k = k%n,n
        return k