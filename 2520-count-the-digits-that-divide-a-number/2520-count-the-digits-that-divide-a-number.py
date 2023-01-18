class Solution:
    def countDigits(self, num: int) -> int:
        splittedList = [int(i) for i in str(num)]
        count = 0
        for i in splittedList:
            if num%i==0:
                count += 1
            else:
                continue
        return count