class Solution(object):
    def firstPalindrome(self, words):
        for word in words:
            word1 = word[::-1]
            if word == word1:
                return word
        return ""