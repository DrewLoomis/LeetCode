class Solution:
    def romanToInt(self, s: str) -> int:
        #results and numberals hashmap for correct matching of roman numerals
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
        #stores the prev value
        prev = 0
        
        for i in s:
            value = numerals[i]
            #for subtraction
            if prev < value:
                #since previous value was added need to subtract twice
                res = res - (2*prev) + value
            else:
                #addition
                res += value
            #loop
            prev = numerals[i]
        #return result
        return res

        
