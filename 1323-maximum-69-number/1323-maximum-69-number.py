class Solution:
    def maximum69Number (self, num: int) -> int:
        numLen = len(str(num))
        for i in range(numLen+1):
            if str(num//10**(numLen-1-i))[-1] == "6":
                num += 3*10**(numLen-1-i)
                return num
        return num
            