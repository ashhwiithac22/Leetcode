class Solution(object):
    def reverseWords(self, s):
        s = s.strip() #removes leading and trailing zeros
        print(s)
        words = s.split()
        print(words)
        reversed_words = words[::-1]
        return ' '.join(reversed_words)
        