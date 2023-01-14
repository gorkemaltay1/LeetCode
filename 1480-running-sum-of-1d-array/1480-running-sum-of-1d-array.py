import numpy as np
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return list(np.cumsum(nums))