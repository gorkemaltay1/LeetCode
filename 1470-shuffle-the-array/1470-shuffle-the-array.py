class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        finalList = []
        for i in range(n):
            finalList.append(nums[i])
            finalList.append(nums[i+n])
        return finalList
        