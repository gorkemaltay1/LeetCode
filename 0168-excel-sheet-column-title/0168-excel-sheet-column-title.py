import string
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alphabet = list(string.ascii_uppercase)
        excelColumn = ""
        while columnNumber > 0:
            excelColumn += alphabet[(columnNumber-1)%26]
            columnNumber = (columnNumber-1) // 26
        return excelColumn[::-1]