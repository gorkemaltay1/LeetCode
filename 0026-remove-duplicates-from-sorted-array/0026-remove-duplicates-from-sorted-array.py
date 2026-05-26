class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        max_val = -101
        last_index = 0
        for i in range(len(nums)):
            if nums[i] > max_val:
                max_val = nums[i]
                nums[last_index] = nums[i]
                last_index += 1
        return last_index


