class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = list()
        while len(nums) != 0:
            AliceNum = min(nums)
            nums.remove(AliceNum)
            BobNum = min(nums)
            nums.remove(BobNum)
            arr.append(BobNum)
            arr.append(AliceNum)
        return arr