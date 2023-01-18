class Solution:
    def maximum69Number (self, num: int) -> int:
        strNum = str(num)
        try:
            strNum = strNum[:strNum.index("6")] + "9" + strNum[strNum.index("6") + 1:] 
            return int(strNum)
        except:
            return num
       

            