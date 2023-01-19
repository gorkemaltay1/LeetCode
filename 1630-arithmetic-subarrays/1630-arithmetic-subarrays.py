class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        boolList = []
        returnInt = 0
        for i in range(len(l)):
            tempList = []
            tempList = sorted(nums[l[i]:r[i]+1])
            diff = abs(tempList[0] - tempList[1])
            for j in range(1,len(tempList)):
                if abs(tempList[j-1] - tempList[j]) == diff:
                    returnInt = 1
                else:
                    returnInt = 0
                    break
            boolList.append(True) if returnInt == 1 else boolList.append(False)
        return boolList
                