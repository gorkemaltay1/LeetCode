class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        finalList = list()
        allNumsList = set(nums1+nums2+nums3)
        for i in allNumsList:
            if (i in nums1 and i in nums2) or (i in nums1 and i in nums3) or (i in nums2 and i in nums3):
                finalList.append(i)
            else:
                continue
        return finalList