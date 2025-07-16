class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        numerals = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
        }
        prev = 0
        curr = 0
        for i in s:
            value = numerals[i]
            if prev < value:
                res = res - (2*prev) + value
            else:
                res += value
            prev = numerals[i]

        return res

        