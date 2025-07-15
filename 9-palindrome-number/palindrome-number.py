class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed = str(x)[::-1]
        if (reversed == str(x)):
            return True
        else:
            return False
