class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        splitList = s.split()
        x = len(splitList[-1])
        return x
        