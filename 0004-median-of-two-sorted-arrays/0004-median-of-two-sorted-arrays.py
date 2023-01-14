import statistics
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        finalList = sorted(nums1 + nums2)
        return statistics.median(finalList)        