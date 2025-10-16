class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        for i in range(len(haystack)):
            if (haystack[i] == needle[0]):
                sub = haystack[i:i + len(needle)]  
                if (sub == needle):
                    return i
        return -1
        