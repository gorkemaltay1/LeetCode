from itertools import combinations
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        groupedList = list(combinations(nums,3))
        count = 0
        
        for i in groupedList:
            if i[2] - i[1] == diff and i[1]-i[0] == diff:
                count += 1
        return count        