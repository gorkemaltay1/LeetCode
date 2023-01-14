class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        smallerNums = []
        for i in nums:
            count = 0
            for j in nums:
                if j<i:
                    count += 1
            smallerNums.append(count)
        return smallerNums
            