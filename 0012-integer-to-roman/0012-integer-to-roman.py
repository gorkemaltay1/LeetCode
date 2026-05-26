class Solution:
    def intToRoman(self, num: int) -> str:
        four = "IV"
        nine = "IX"
        forty = 'XL'
        ninety = 'XC'
        fourhundred = 'CD'
        ninehundred = 'CM'
        result = ""
        
        if num // 1000 > 0:
            result += (num // 1000) * 'M'
        if num // 100 % 10 > 0:
            if num // 100 % 10 == 4:
                result += fourhundred
            elif num // 100 % 10 == 9:
                result += ninehundred
            elif num // 100 % 10 >= 0 and num // 100 % 10 < 5:
                result += (num // 100 % 10) * "C"
            elif num // 100 % 10 >= 5:
                result += 'D' + ((num // 100 % 10) % 5) * 'C'
        if num // 10 % 10 > 0:
            if num // 10 % 10 == 4:
                result += forty
            elif num // 10 % 10 == 9:
                result += ninety
            elif num // 10 % 10 >= 0 and num // 10 % 10 < 5:
                result += (num // 10 % 10) * "X"
            elif num // 10 % 10 >= 5:
                result += 'L' + ((num // 10 % 10) % 5) * 'X'
        if num % 10 > 0:
            if num % 10 == 4:
                result += four
            elif num % 10 == 9:
                result += nine
            elif num % 10 >= 0 and num % 10 < 5:
                result += (num % 10) * "I"
            elif num % 10 >= 5:
                result += 'V' + ((num % 10) % 5) * 'I'


        return result
