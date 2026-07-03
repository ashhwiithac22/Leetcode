class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = {}
        for char in text:
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1
        if 'b' not in freq or 'a' not in freq or 'l' not in freq or 'o' not in freq or 'n' not in freq:
            return 0
        b = freq['b'] // 1
        a = freq['a'] // 1
        l = freq['l'] // 2
        o = freq['o'] // 2
        n = freq['n'] // 1
        return min(b, a, l, o, n)

