from math import factorial
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        finalList = list()
        for i in range(numRows):
            rowList = list()
            for j in range(i+1):
                rowList.append(int(factorial(i)/(factorial(i-j)*factorial(j))))
            finalList.append(rowList)
        return finalList