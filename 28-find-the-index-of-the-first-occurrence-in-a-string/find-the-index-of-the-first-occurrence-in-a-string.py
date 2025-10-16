class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        for i in range(len(haystack)):
            if (haystack[i] == needle[0]):
                #print(i)
                sub = haystack[i:i + len(needle)]  
                print(sub)
                print(needle)
                #print(len(needle))
                print(sub == needle)
                if (sub == needle):
                    print(True)
                    return i
                else:
                    print("false")
        return -1
        