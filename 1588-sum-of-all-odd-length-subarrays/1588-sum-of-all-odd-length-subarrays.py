from itertools import combinations
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        sumOddLength = 0
        for i in range(1,len(arr)+1,2):
            for j in range(int(len(arr)-i+1)):
                sumOddLength += sum(arr[j:i+j])
        return sumOddLength
                
            
            