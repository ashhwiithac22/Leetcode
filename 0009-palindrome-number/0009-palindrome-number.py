class Solution(object):
    def isPalindrome(self, x):
       a = str(x)
       if str(x) == a[::-1]:
        return True
       else:
        return False