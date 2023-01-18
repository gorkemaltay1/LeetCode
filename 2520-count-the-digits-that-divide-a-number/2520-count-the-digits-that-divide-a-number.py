class Solution:
    def countDigits(self, num: int) -> int:
        a = num
        splittedList = []
        while a > 0:
            splittedList.append(a%10)
            a = a // 10
            
        count = 0
        for i in splittedList:
            if num%i==0:
                count += 1
            else:
                continue
        return count