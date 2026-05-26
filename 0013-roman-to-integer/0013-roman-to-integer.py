class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            "M":1000,
            'D':500,
            'C':100,
            'L':50,
            'X':10,
            'V':5,
            'I':1
        }
        special_ones = {
            'IV':4,
            'IX':9,
            'XL':40,
            'XC':90,
            'CD':400,
            'CM':900
        }

        #MMCMXCIV
        result = 0

        for i in range(len(s)):
            if i != len(s) - 1:
                if roman_dict[s[i-1]] < roman_dict[s[i]] and i != 0:
                    continue
                if roman_dict[s[i+1]] > roman_dict[s[i]]:
                    result += special_ones[s[i:i+2]]
                    print(special_ones[s[i:i+2]])
                else:
                    result += roman_dict[s[i]]
                    print(roman_dict[s[i]])
        if s[-2:] not in list(special_ones.keys()):
            result += roman_dict[s[-1]]


        return result