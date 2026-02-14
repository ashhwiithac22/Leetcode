class Solution(object):
    def isPalindrome(self, s):
        lowercase = ""
        for ch in s:
            if ch.isalnum():
                lowercase += ch.lower()
        return lowercase == lowercase[::-1]