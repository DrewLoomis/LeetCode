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
        for a, b in zip(s, s[1:]):
            if numerals[a] < numerals[b]:
                res -= numerals[a]
            else:
                res += numerals[a]

        return res + numerals[s[-1]] 

        