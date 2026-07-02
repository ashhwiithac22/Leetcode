class Solution:
    def isSubsequence(self, s: str, t: str):
        k = 0
        for i in range(len(s)):
            for j in range(k, len(t)):
                if s[i] == t[j]:
                    k = j + 1
                    break
            else:
                return False
        return True
