class Solution:
    def isPalindrome(self, x: int) -> bool:
        #convert int to str and then reverse
        reversed = str(x)[::-1]
        #if we have a palindrome
        if (reversed == str(x)):
            return True
        else:
            return False
